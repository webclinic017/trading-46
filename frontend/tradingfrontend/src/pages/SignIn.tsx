import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { Alert } from '@mui/lab';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import * as yup from "yup";
import { useFormik } from "formik";
import { useState } from "react";
import axios from "axios";
import { useNavigate, NavLink } from 'react-router-dom';
import { AUTH_API_NODE } from "../constants/index"
import CancelIcon from '@mui/icons-material/Cancel';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { GoogleLogin } from '@react-oauth/google';
import { googleLogout } from '@react-oauth/google';

function Copyright(props: any) {
    return (
        <Typography variant="body2" color="text.secondary" align="center" {...props}>
            {'Copyright © '}
            <Link color="inherit" href="https://mui.com/">
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const theme = createTheme();

export default function SignInSide() {
    const validationSchema = yup.object({
        email: yup
            .string()
            .email("請輸入有效電子郵件")
            .required("電子郵件是必填欄位"),
        password: yup.string().required("密碼是必填欄位"),
    });

    // const { switchToSignup } = useContext(AccountContext);

    const [errorcode, setErrorcode] = useState(false);

    const onSubmit = async (values) => {
        const response = await axios
            .post(AUTH_API_NODE + "/login", values)
            .catch((err) => {
                if (err.response.data.error_code === "1010002") {
                    setErrorcode(true);
                    setShowAlert("電子郵件尚未註冊，請重新輸入。");

                    //console.log(err.error_code);
                    setTimeout(() => {
                        setErrorcode(false);
                        setShowAlert(null);
                    }, 3000);
                } else if (err.response.data.error_code === "1010003") {
                    setErrorcode(true);

                    setShowAlert("登入密碼輸入錯誤，請重新輸入。");

                    //console.log(err.response.data.detail);
                    setTimeout(() => {
                        setErrorcode(false);

                        setErrorcode(null);
                        setShowAlert(null);
                    }, 3000);
                }
            });

        if (response) {
            history.push("/loading");
            localStorage.setItem("accessToken", response.data.access_token);
            // alert("Welcome back in. Authenticating...");
            //console.log(response);
        }
    };

    const formik = useFormik({
        initialValues: { email: "", password: "" },
        validateOnBlur: true,
        onSubmit,
        validationSchema: validationSchema,
    });

    const history = useNavigate();

    const [showAlert, setShowAlert] = useState(null);

    const [state, setState] = useState({
        checkedB: false,
    });

    const handleChangeCheckBox = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

    if (state.checkedB === true) {
        const email = formik.values.email;
        localStorage.setItem("useremail", email);
    }
    if (localStorage.getItem("useremail")) {
        formik.initialValues.email = localStorage.getItem("useremail");
    }

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        console.log({
            email: data.get('email'),
            password: data.get('password'),
        });
    };

    return (
        <ThemeProvider theme={theme}>
            <Grid container component="main" sx={{ height: '100vh' }}>
                <GoogleOAuthProvider clientId="219527937106-iv4ete3gb2i5867pgv8ue0vbaneakbvp.apps.googleusercontent.com">
                    <CssBaseline />
                    <Grid
                        item
                        xs={false}
                        sm={4}
                        md={7}
                        sx={{
                            backgroundImage: 'url(https://source.unsplash.com/random)',
                            backgroundRepeat: 'no-repeat',
                            backgroundColor: (t) =>
                                t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
                            backgroundSize: 'cover',
                            backgroundPosition: 'center',
                        }}
                    />
                    <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
                        <Box
                            sx={{
                                my: 8,
                                mx: 4,
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
                            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1 }}>
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    name="email"
                                    autoFocus
                                    variant="outlined"
                                    id="input"
                                    label="請輸入電子郵件"
                                    value={formik.values.email}
                                    type="input"
                                    onChange={formik.handleChange}
                                    autoComplete="current-password"
                                    helperText={
                                        formik.touched.email && formik.errors.email
                                            ? formik.errors.email
                                            : ""
                                    }
                                    onBlur={formik.handleBlur}
                                    error={
                                        (formik.touched.email && Boolean(formik.errors.email)) ||
                                        errorcode
                                    }
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    name="password"
                                    type="password"
                                    id="filled-password-input"
                                    label="請輸入密碼"
                                    onChange={formik.handleChange}
                                    onBlur={formik.handleBlur}
                                    helperText={
                                        formik.touched.password && formik.errors.password
                                            ? formik.errors.password
                                            : ""
                                    }
                                    // onChange={handleChange('Password')}
                                    autoComplete="current-password"
                                    variant="outlined"
                                    error={
                                        (formik.touched.email && Boolean(formik.errors.email)) ||
                                        errorcode
                                    }
                                />
                                <FormControlLabel
                                    control={<Checkbox checked={state.checkedB}
                                        onChange={handleChangeCheckBox}
                                        name="checkedB"
                                        value="remember"
                                        color="primary" />}
                                    label="記住登入資訊"
                                />
                                <Button
                                    type="submit"
                                    fullWidth
                                    variant="contained"
                                    sx={{ mt: 3, mb: 2 }}
                                >
                                    登入
                                </Button>
                                <GoogleLogin
                                    width='100%'
                                    onSuccess={credentialResponse => {
                                        console.log(credentialResponse);
                                    }}
                                    onError={() => {
                                        console.log('Login Failed');
                                    }}
                                />
                                <Button onClick={() => {
                                    googleLogout();
                                }}>
                                    google logout
                                </Button>
                                <Grid container>
                                    <Grid item xs>
                                        <NavLink
                                            to="/ForgetPassword"
                                            style={{ textDecoration: "none" }}
                                            className="paragraphSmall regular link_Text"
                                        >
                                            忘記密碼?
                                        </NavLink>
                                    </Grid>
                                    <Grid item>
                                        <NavLink
                                            to="/signup"
                                            style={{ textDecoration: "none" }}
                                            className="paragraphSmall regular link_Text"
                                        >
                                            {"還沒有帳號? 註冊"}
                                        </NavLink>
                                    </Grid>
                                </Grid>
                                <div className="Alert_Middle">
                                    {errorcode ? (
                                        <Alert
                                            icon={<CancelIcon />}
                                            style={{
                                                padding: "0px",
                                                color: "#DA1414",
                                                fontFamily: " Noto Sans CJK TC",
                                            }}
                                            className="Alert_Middle"
                                            severity="error"
                                        >
                                            {showAlert}
                                        </Alert>
                                    ) : null}
                                </div>
                                <Copyright sx={{ mt: 5 }} />
                            </Box>
                        </Box>
                    </Grid>
                </GoogleOAuthProvider >
            </Grid>
        </ThemeProvider>
    );
}
