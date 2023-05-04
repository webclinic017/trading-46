import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Alert } from '@mui/lab';
import * as yup from "yup";
import { useFormik } from "formik";
import { useState } from "react";
import axios from "axios";
import { useNavigate, NavLink } from 'react-router-dom';
import { AUTH_API_NODE } from "../constants/index"
import CancelIcon from '@mui/icons-material/Cancel';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
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

export default function SignUp() {
    const PASSWORD_REGEX = /^.{6,14}$/;
    const Fullname_REGEX = /^[\u4e00-\u9fa5_a-zA-Z0-9/@+~`<>]+$/;
    // /#\?\!%\^+/
    // const containsDeviceId = (string) => /#\?\!%\^+/.test(string);

    const validationSchema = yup.object({
        fullName: yup
            .string()
            .max(14, "用戶名稱格式不正確")
            .matches(Fullname_REGEX, "用戶名稱格式不正確")
            .required("使用者名稱是必填欄位"),
        // .test("用戶名稱格式不正確","用戶名稱格式不正確",(value) => !containsDeviceId(value)),
        email: yup
            .string()
            .email("電子郵件格式不正確")
            .required("電子郵件是必填欄位"),
        password: yup
            .string()
            .matches(PASSWORD_REGEX, "密碼不符合規則")
            .required("密碼是必填欄位"),
        confirmPassword: yup
            .string()
            .required("請再次輸入密碼")
            .oneOf([yup.ref("password")], "重複密碼輸入錯誤")
        ,
        toggle: yup.bool().oneOf([true], "*需勾選"),
    });
    // const { switchToSignin } = useContext(AccountContext);
    const [errorcode, setErrorcode] = useState(false);
    const [colorCode, setcolorCode] = useState(false);
    const onSubmit = async (values) => {
        const { confirmPassword, toggle, ...data } = values;
        const checkInternetConnection = await axios.interceptors.response.use(
            (response) => {
                return response;
            },
            (error) => {
                if (!error.response) {
                    setcolorCode(false);
                    setOpen(true);
                    setSnackbarSeverity("error");
                    setAlertText("網路連線異常，請稍後再試。");
                    setTimeout(() => {
                        setcolorCode();
                        setOpen(false);
                    }, 3000);
                }
                return Promise.reject(error);
            }
        )
        const response = await axios
            .post(AUTH_API_NODE + "sign-up", data)
            .catch((err) => {
                if (err.response.data.error_code === "1010004") {
                    setcolorCode(false);
                    setOpen(true);
                    setErrorcode(true);
                    setSnackbarSeverity("error");
                    setAlertText("電子郵件信箱已被註冊，請更換註冊信箱。");
                    setTimeout(() => {
                        setcolorCode();
                        setErrorcode(false);
                        setOpen(false);
                    }, 3000);
                }
                else if (err.response.data.error_code === "404") {
                    setcolorCode(false);
                    setOpen(true);
                    setErrorcode(true);
                    setSnackbarSeverity("error");
                    setAlertText("伺服器錯誤，請稍後再試。");
                    setTimeout(() => {
                        setcolorCode();
                        setErrorcode(false);
                        setOpen(false);
                    }, 3000);
                }
                else  
                    setcolorCode(false);
                    setOpen(true);
                    setErrorcode(true);
                    setSnackbarSeverity("error");
                    setAlertText("伺服器錯誤，請稍後再試。");
                    setTimeout(() => {
                        setcolorCode();
                        setErrorcode(false);
                        setOpen(false);
                    }, 3000);
            }

            );

        if (response && response.data) {
            //console.log(response);
            setcolorCode(true);
            setSnackbarSeverity("success");
            setAlertText("帳號註冊完成，3秒內將自動返回登入頁面。");
            setTimeout(() => {
                history("/");
            }, 3000);
        }
    };

    const formik = useFormik({
        initialValues: {
            email: "",
            fullName: "",
            password: "",
            confirmPassword: "",
            toggle: false,
        },
        validateOnBlur: true,
        onSubmit,
        validationSchema: validationSchema,
    });

    const [opencode, setOpen] = useState(false);
    const [AlertText, setAlertText] = useState(null);
    const [snackbarSeverity, setSnackbarSeverity] = useState("");
    // //console.log("Error", error);
    const history = useNavigate();
    // const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    //     event.preventDefault();
    //     const data = new FormData(event.currentTarget);
    //     console.log({
    //         email: data.get('email'),
    //         password: data.get('password'),
    //     });

    // };
return (
    <ThemeProvider theme={theme}>
        <Container component="main" maxWidth="xs">
            <CssBaseline />
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
                終極股市回測王 註冊頁面
                </Typography>
                <Box component="form" noValidate onSubmit={formik.handleSubmit} sx={{ mt: 3 }}>
                    <Grid container spacing={2}>
                        <Grid item xs={12} >
                            <TextField
                                autoComplete="given-name"
                                fullWidth
                                label="使用者名稱"
                                autoFocus
                                name="fullName"
                                id="filled-input"
                                placeholder="請輸入14個字以元下名稱，不可使用#?!%^符號。"
                                value={formik.values.fullName}
                                type="input"
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}
                                variant="outlined"
                                error={
                                    formik.touched.fullName && Boolean(formik.errors.fullName)
                                }
                                helperText={
                                    formik.touched.fullName && formik.errors.fullName
                                        ? formik.errors.fullName
                                        : ""
                                }
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="電子信箱"
                                name="email"
                                autoComplete="email"
                                id="filled-input"
                                placeholder="請輸入您的電子郵件信箱"
                                value={formik.values.email}
                                type="input"
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}
                                variant="outlined"
                                // error={errorcode}
                                error={
                                    (formik.touched.email && Boolean(formik.errors.email)) ||
                                    errorcode
                                }
                                helperText={
                                    formik.touched.email && formik.errors.email
                                        ? formik.errors.email
                                        : ""
                                }
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                name="password"
                                label="密碼"
                                type="password"
                                id="password"
                                autoComplete="new-password"
                                placeholder="請輸入6~14個字元登入密碼"
                                value={formik.values.password}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}
                                variant="outlined"
                                color="primary"
                                error={
                                    formik.touched.password && Boolean(formik.errors.password)
                                }
                                helperText={
                                    formik.touched.password && formik.errors.password
                                        ? formik.errors.password
                                        : ""
                                }
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                label="確認密碼"
                                id="filled-password-input"
                                placeholder="請再次輸入設定密碼"
                                name="confirmPassword"
                                type="password"
                                value={formik.values.confirmPassword}
                                onChange={formik.handleChange}
                                onBlur={formik.handleBlur}
                                autoComplete="current-password"
                                variant="outlined"
                                color="primary"
                                error={
                                    formik.touched.confirmPassword &&
                                    Boolean(formik.errors.confirmPassword)
                                }
                                helperText={
                                    formik.touched.confirmPassword &&
                                        formik.errors.confirmPassword
                                        ? formik.errors.confirmPassword
                                        : ""
                                }
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <FormControlLabel
                                control={
                                    <Checkbox
                                        checked={formik.values.toggle}
                                        value={formik.values.toggle}
                                        onChange={formik.handleChange}
                                        onBlur={formik.handleBlur}
                                        name="toggle"
                                        color="default"
                                    />
                                }
                                label={
                                    <Typography>
                                        "我同意 使用者使用條款"
                                    </Typography>
                                }
                            />
                        </Grid>
                    </Grid>
                    <Button
                        fullWidth={true}
                        type="submit"
                        disabled={!formik.isValid}
                        variant="contained"
                        color="primary"
                        disableRipple
                    >
                        完成註冊
                    </Button>
                    <Grid container justifyContent="flex-end">
                        <Grid item>
                            <NavLink to="/" style={{ textDecoration: "none" }}>
                                已經擁有帳號? 返回至登入頁面。
                            </NavLink>
                        </Grid>
                    </Grid>
                    {colorCode ? (
                        <Alert
                            icon={<CheckCircleIcon />}
                            style={{
                                padding: "0px",
                                color: "#287D3C",
                                justifyContent: "center",
                                fontFamily: " Noto Sans CJK TC",
                            }}
                            className="Alert_Middle"
                            severity={snackbarSeverity}
                        >
                            {AlertText}
                        </Alert>
                    ) : (
                        <></>
                    )}

                    {opencode ? (
                        <Alert
                            icon={<CancelIcon />}
                            style={{
                                padding: "0px",
                                color: "#DA1414",
                                justifyContent: "center",
                                fontFamily: " Noto Sans CJK TC",
                            }}
                            className="Alert_Middle"
                            severity={snackbarSeverity}
                        >
                            {AlertText}
                        </Alert>
                    ) : (
                        <></>
                    )}
                </Box>
            </Box>
            <Copyright sx={{ mt: 5 }} />
        </Container>
        </ThemeProvider >
    );
}
