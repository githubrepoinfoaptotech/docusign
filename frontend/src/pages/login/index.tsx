import React from "react";
import { Avatar, Box, Button, Container, TextField, Typography, Grid, Link } from "@mui/material";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import animationData from "../../lotties/Animation - 1718956006634.json";
import "./login.css"
import Lottie from 'react-lottie';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { Form, Formik, FormikProps, FormikValues, ErrorMessage } from "formik";
import * as yup from "yup"
import Axios from "../../configs/AxiosConfig";
import { AxiosError, AxiosResponse } from "axios";
// import { useNavigate } from "react-router-dom";
import { Notify } from "notiflix";

const theme = createTheme();

interface IloginValues {
  username: string
  password: string
}


const Login: React.FC = () => {

  // const navigate=useNavigate();

  const handleSubmit = (values: FormikValues) => {
    console.log(values);
    Axios.post("user/login",values).then((data:AxiosResponse)=>{
      console.log(data.data);
      if(data.data.status){
        Notify.success(data.data.message);
        // setTimeout(()=>navigate("/dashboard"),500);
      }
    }).catch((err:AxiosError)=>{
      console.log(err);
    })
  };

  const initialValues: IloginValues = {
    username: "",
    password: ""
  }

  const validationSchema: yup.ObjectSchema<IloginValues> = yup.object({
    username: yup.string().email().required(),
    password: yup.string().required()
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
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Formik

              initialValues={initialValues}
              validationSchema={validationSchema}
              onSubmit={handleSubmit}

            >
              {((formik: FormikProps<IloginValues>) => (
                <Form>
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    id="username"
                    label="Username"
                    name="username"
                    autoComplete="username"
                    autoFocus
                    value={formik.values.username}
                    onChange={formik.handleChange}
                  />
                  
                  <ErrorMessage name="username" component="div" />
                 
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
                  
                  <ErrorMessage name="password" component="div" />
                 
                  <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    sx={{ mt: 3, mb: 2 }}
                  >
                    Sign In
                  </Button>
                </Form>
              ))}
            </Formik>

            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/signup" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Container>
      </ThemeProvider>
    </Box>

  );
};

export default Login;