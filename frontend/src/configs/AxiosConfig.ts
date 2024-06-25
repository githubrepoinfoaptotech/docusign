import axios,{ AxiosInstance, AxiosRequestConfig } from "axios";
import { Notify } from "notiflix";

const axiosConfig:AxiosRequestConfig={
    baseURL:"http://localhost:5000/api/",
    timeout:10000,
    headers:{
        "Content-Type":"application/json"
    }
}

const Axios:AxiosInstance=axios.create(axiosConfig)

Axios.interceptors.response.use(
    (response)=>response,
    (error)=>{
        if (error.response && error.response.status === 401) {
            console.log(error);
        }

        Notify.failure(error.response.data.message);

        return Promise.reject(error);
    }
)

export default Axios;