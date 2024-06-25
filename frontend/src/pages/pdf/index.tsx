import React, { useEffect, useRef, useState } from 'react';
import * as PdfjsLib from "pdfjs-dist";
import { RenderParameters } from 'pdfjs-dist/types/src/display/api';

// Set the worker file path
// PdfjsLib.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/4.3.136/pdf.min.mjs`;
PdfjsLib.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@4.3.136/build/pdf.worker.min.mjs`;



interface IpdfUrl {
    path: string;
}

const PdfViewer: React.FC<IpdfUrl> = (props) => {
    const pdfCanvasRef = useRef<HTMLCanvasElement>(null);
    const [isSet, setIsSet] = useState<boolean>(false);
    const [renderTask, setRenderTask] = useState<PdfjsLib.RenderTask | null>(null);

    useEffect(() => {
        const loadPdf = async () => {
            try {
                const pdfDoc: PdfjsLib.PDFDocumentLoadingTask = PdfjsLib.getDocument(props.path);
                const pdf = await pdfDoc.promise;

                if (pdfCanvasRef.current && (!isSet)) {
                    const canvas = pdfCanvasRef.current;
                    const context = canvas.getContext('2d');
                    if (context) {
                        const page = await pdf.getPage(1);
                        const viewport = page.getViewport({ scale: 1.0 });

                        canvas.width = viewport.width;
                        canvas.height = viewport.height;

                        if (renderTask) {
                            await renderTask.cancel();
                        }

                        const renderContext: RenderParameters = {
                            canvasContext: context,
                            viewport: viewport,
                        };

                        const task = page.render(renderContext);
                        setRenderTask(task);

                        await task.promise;

                        canvas.addEventListener('mousedown', (event) => {
                            const canvasX = event.offsetX;
                            const canvasY = event.offsetY;

                            const pdfX = (canvasX / canvas.width) * viewport.width;
                            const pdfY = (canvasY / canvas.height) * viewport.height;

                            console.log(`Clicked PDF coordinates: (x=${canvasX - 100}, y=${680 - canvasY} | ${pdfX}, ${pdfY})`);
                            setIsSet(true);
                        });
                    }
                }
            } catch (error) {
                console.error('Error loading PDF:', error);
            }
        };

        loadPdf();

        return () => {
            if (renderTask) {
                renderTask.cancel();
            }
        };
    }, [props.path]);

    return (
        <div>
            <canvas ref={pdfCanvasRef}></canvas>
        </div>
    );
};

export default PdfViewer;