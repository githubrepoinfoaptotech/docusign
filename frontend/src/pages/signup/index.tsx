import React from "react";
import { Avatar, Box, Button, Container, TextField, Typography, Grid, Link } from "@mui/material";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import animationData from "../../lotties/signup.json";
import Lottie from 'react-lottie';
import AssignmentIndIcon from '@mui/icons-material/AssignmentInd';
import { Formik, Form, FormikValues, ErrorMessage, FormikProps } from "formik";
import * as yup from "yup"
import Axios from "../../configs/AxiosConfig";
import { AxiosError, AxiosResponse } from "axios";
import { Notify } from "notiflix";
import { useNavigate } from "react-router-dom";

const theme = createTheme();

interface ISignupValues {
    username: string
    password: string
    fullname: string
    initial: string
}

const Signup: React.FC = () => {

    const navigate = useNavigate();

    const handleSubmit = (values: FormikValues) => {
        console.log(values);
        // onLogin(username, password);
        Axios.post("user/register",values).then((data:AxiosResponse)=>{
            if(data.data?.status){
                Notify.success(data.data.message);
                setTimeout(()=>{navigate("/login")},1000);
            }
        }).catch((err:AxiosError)=>{
            if(err.response?.status==409){
                setTimeout(()=>{ navigate("/login")},1000);
            }
        })
    };

    // const handleChange = (values) => {
    //     console.log(values);
    //     // onLogin(username, password);
    // };

    const initialValues: ISignupValues = {
        username: "",
        password: "",
        fullname: "",
        initial: ""
    }

    const ValidationSchema: yup.ObjectSchema<ISignupValues> = yup.object({
        username: yup.string().email().required(),
        password: yup.string().required(),
        fullname: yup.string().required().min(3),
        initial: yup.string().required().max(2)
    })


    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: animationData,
        rendererSettings: {
            preserveAspectRatio: 'xMidYMid slice'
        }
    };

    return (
        <Box sx={{ display: "flex", flex: 1 }} >

            <Lottie options={defaultOptions}
                height={500}
                width={500}
            />
            <ThemeProvider theme={theme}>
                <Container component="main" maxWidth="xs">
                    <Box
                        sx={{
                            marginTop: 8,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                        }}
                    >
                        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                            <AssignmentIndIcon />
                        </Avatar>
                        <Typography component="h1" variant="h5">
                            Sign Up
                        </Typography>
                        <Formik
                            initialValues={initialValues}
                            validationSchema={ValidationSchema}
                            onSubmit={handleSubmit}
                        >
                            {(formik: FormikProps<ISignupValues>) => 
                            
                            (
                                <Form>
                                    <Box sx={{ display: "flex", gap: "5px" }} >
                                        <TextField
                                            margin="normal"
                                            required
                                            // fullWidth
                                            sx={{ width: "70%" }}
                                            id="fullname"
                                            label="Full Name"
                                            autoFocus
                                            name="fullname"
                                            autoComplete="fullname"
                                            value={formik.values.fullname}
                                            onChange={formik.handleChange}
                                        />
                                        <TextField
                                            margin="normal"
                                            required
                                            // fullWidth
                                            sx={{ width: "30%" }}
                                            id="initial"
                                            label="Initial"
                                            name="initial"
                                            autoComplete="initial"
                                            value={formik.values.initial}
                                            onChange={formik.handleChange}
                                        />
                                    </Box>
                                    <Box sx={{ display: "flex", gap: "5px" }} >
                                        <Box sx={{ width: "70%" }} >

                                            <ErrorMessage className="error" name="fullname" component="div" />
                                        </Box>
                                        <Box sx={{ width: "30%" }} >

                                            <ErrorMessage className="error" name="initial" component="div" />
                                        </Box>

                                    </Box>
                                    <TextField
                                        margin="normal"
                                        required
                                        fullWidth
                                        id="username"
                                        label="Username"
                                        name="username"
                                        autoComplete="username"
                                        value={formik.values.username}
                                        onChange={formik.handleChange}

                                    />
                                    <ErrorMessage className="error" name="username" component="div" />
                                    <TextField
                                        margin="normal"
                                        required
                                        fullWidth
                                        name="password"
                                        label="Password"
                                        type="password"
                                        id="password"
                                        autoComplete="current-password"
                                        value={formik.values.password}
                                        onChange={formik.handleChange}
                                    />
                                    <ErrorMessage className="error" name="password" component="div" />


                                    <Button
                                        type="submit"
                                        fullWidth
                                        variant="contained"
                                        sx={{ mt: 3, mb: 2 }}
                                    >
                                        Sign Up
                                    </Button>
                                </Form>
                            )}

                        </Formik>
                        <Grid container>
                            {/* <Grid item xs>
                                    <Link href="#" variant="body2">
                                        Forgot password?
                                    </Link>
                                </Grid> */}
                            <Grid item>
                                <Link href="#" variant="body2">
                                    Already have an account? Sign In
                                </Link>
                            </Grid>
                        </Grid>

                    </Box>
                </Container>
            </ThemeProvider>
        </Box>

    );
};

export default Signup;