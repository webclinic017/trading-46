import { Typography } from "@material-ui/core";
// // 修飾輸入框套件
// import clsx from 'clsx';
// import FilledInput from '@material-ui/core/FilledInput';
// import OutlinedInput from '@material-ui/core/OutlinedInput';
// import InputLabel from '@material-ui/core/InputLabel';
// import InputAdornment from '@material-ui/core/InputAdornment';
// import FormHelperText from '@material-ui/core/FormHelperText';
// import FormControl from '@material-ui/core/FormControl';
// import Visibility from '@material-ui/icons/Visibility';
// import VisibilityOff from '@material-ui/icons/VisibilityOff';
// import Grid from '@material-ui/core/Grid';
// import Input from '@material-ui/core/Input';
// import IconButton from '@material-ui/core/IconButton';
// import {alpha} from '@material-ui/styles';
// //勾選記住帳號資訊套件
// import Checkbox from '@material-ui/core/Checkbox';
//按鈕
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { makeStyles, withStyles } from "@material-ui/styles";
//login套件
import axios from "axios";
import { useFormik } from "formik";
import React, { useState } from "react";
//頁面跳轉
import { NavLink, useHistory } from "react-router-dom";
import * as yup from "yup";
import * as Constant from "../components/Constant";
import "../css/All.css";
import Imagewelcome from "../components/Images/ImageWelcome.png";






const CssTextField = withStyles({
  root: {
    // '& label.Mui-focused': {
    //   color: '#2C82FF',
    // },
    "& .MuiInput-underline:after": {
      borderBottomColor: "green",
    },
    "& .MuiOutlinedInput-root": {
      "& fieldset": {
        borderRadius: `8px 8px 8px 8px`,
        border: "1px,solid",
        boxShadow: "0px 4px 10px rgba(25, 1, 52, 0.16)",
        borderColor: "#CFCFCF",
      },
      "&:hover fieldset": {
        border: "10px,solid",
        backgroundColor: "none",
        borderColor: "#5D5D5D",
        boxShadow: "0px 4px 10px rgba(25, 1, 52, 0.16)",
      },
      "&.Mui-focused fieldset": {
        borderColor: "#0957C3",
        backgroundColor: "none",
      },
      "&:error fieldset": {
        borderColor: "#ff0000",
      },
    },
  },
})(TextField);

function App() {
  const useClasses = makeStyles((theme) => ({
    root: {
      display: "flex",
      flexWrap: "wrap",
    },
    textField: {
      height: "55px",
      width: "400px",
      borderRadius: `8px 8px 8px 8px`,
      padding: "0px, 0px, 0px, 0px",
      borderColor: "#0957C3",
      backgroundColor: "#fff",
      boxShadow: "0px 4px 10px rgba(25, 1, 52, 0.16)",
      "&:hover": {
        border: "3px,solid",
        backgroundColor: "none",
        borderColor: "#5D5D5D",
        boxShadow: "0px 4px 10px rgba(25, 1, 52, 0.16)",
      },
      "&:active": {
        borderColor: "#fff",
        backgroundColor: "none",
      },
      "&:focus": {
        borderColor: "#fff",
        color: "none",
        backgroundColor: "none",
      },
    },
    helperText: {
      color: "#ff0000",
      fontFamily: ["Noto Sans CJK TC"],
    },
    label: {
      fontFamily: ["Noto Sans CJK TC"],
    },
  }));
  const classes = useClasses();
  //checkbox

  const BlackTextTypography = withStyles({
    root: {
      color: "#5D5D5D",
      fontSize: "14px",
      fontFamily: ["Noto Sans CJK TC"].join(","),
    },
  })(Typography);


  //輸入欄顏色

  //按鈕顏色
  const BootstrapButtonlogin = withStyles({
    root: {
      boxShadow: "none",
      width: "184px",
      height: "48px",
      textTransform: "none",
      fontSize: 18,
      padding: "0px 0px",
      border: "1px solid",
      lineHeight: 1.5,
      backgroundColor: "#0957C3",
      borderColor: "none",
      fontFamily: ["Noto Sans CJK TC"].join(","),
      "&:hover": {
        backgroundColor: "#307FE2",
        borderColor: "none",
        boxShadow: "none",
        fontcolor: "#0957C3",
      },
      "&:active": {
        boxShadow: "none",
        backgroundColor: "#0957C3",
        borderColor: "#0957C3",
      },
      "&:focus": {
        boxShadow: "0 0 0 0.2rem ",
      },
      "&:disabled": {
        color: "#E4E3E2",
        backgroundColor: "#0957C3",
      },
    },
  })(Button);


  //Theme顏色






  const [errorcode, setErrorcode] = useState(false);
  const PASSWORD_REGEX = /^.{6,14}$/;

  const validationSchema = yup.object({
    fullName: yup
      .string()
      .min(3, "請輸入使用者名稱")
      .required("使用者名稱是必填欄位"),
    email: yup
      .string()
      .email("請輸入有效電子郵件")
      .required("電子郵件是必填欄位"),
    password: yup
      .string()
      .matches(PASSWORD_REGEX, "密碼不符合規則")
      .required("密碼是必填欄位"),
    confirmPassword: yup
      .string()
      .required("請再次輸入密碼")
      .when("password", {
        is: (val) => (val && val.length > 0 ? true : false),
        then: yup.string().oneOf([yup.ref("password")], "重複密碼輸入錯誤"),
      }),
    toggle: yup.bool().oneOf([true], "*需勾選"),
  });
  // const { switchToSignin } = useContext(AccountContext);

  const onSubmit = async (values) => {
    const { confirmPassword, ...data } = values;

    const response = await axios
      .post(Constant.AUTH_API_NODE + "/sign-up", data)
      .catch((err) => {
        if (err && err.response === "401")
        //console.log(err);
        setErrorcode(true);
      });

    if (response && response.data) {
      //console.log(response);
      formik.resetForm();
 
      setTimeout(() => {
        history.push("/");
      }, 5000);
    }
  };

  const formik = useFormik({
    initialValues: {
      fullName: "",
      email: "",
      password: "",
      confirmPassword: "",
      toggle: false,
    },
    validateOnBlur: true,
    onSubmit,
    validationSchema: validationSchema,
  });

  const history = useHistory();

  return (
    <div className="container-center-horizontal">
      <div className="mainscreen">
        <img className="layoutLeft" src={Imagewelcome} alt="" />
        <div className="layoutRight">
          <div className="infoResetPassword">
            <div className="lebel_Title h2 heavy">無人機橋梁檢測系統(DBIS)</div>
            <div className="lebelhint h6 regular">
              請輸入新密碼，並再次輸入確認更改。
            </div>

            <div className="enterColumn1">
              <CssTextField
                id="filled-password-input"
                label="請輸入6~14個字元登入密碼"
                name="password"
                type="password"
                className={classes.textField}
                value={formik.values.password}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                autoComplete="current-password"
                variant="outlined"
                color="primary"
                error={errorcode}
                helperText={
                  formik.touched.password && formik.errors.password
                    ? formik.errors.password
                    : ""
                }
                InputLabelProps={{
                  className: classes.label,
                }}
                FormHelperTextProps={{
                  className: classes.helperText,
                }}
              />
            </div>
            <div className="enterColumn4">
              <CssTextField
                id="filled-password-input"
                label="請再次輸入密碼"
                name="confirmPassword"
                type="password"
                className={classes.textField}
                value={formik.values.confirmPassword}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                autoComplete="current-password"
                variant="outlined"
                color="primary"
                error={errorcode}
                helperText={
                  formik.touched.confirmPassword &&
                  formik.errors.confirmPassword
                    ? formik.errors.confirmPassword
                    : ""
                }
                FormHelperTextProps={{
                  className: classes.helperText,
                }}
                InputLabelProps={{
                  className: classes.label,
                }}
              />
            </div>

            <div className="buttonsForgetPassword">
              <BootstrapButtonlogin
                variant="contained"
                color="primary"
                disableRipple
                className={classes.margin}
                // onClick={handleServerItemsLoad}
                onClick={() => history.push("/")}
              >
                確認更改密碼
              </BootstrapButtonlogin>
            </div>
            <div className="labelReturn">
              {" "}
              <NavLink to="/" style={{ textDecoration: "none" }}>
                <BlackTextTypography>返回登入頁面</BlackTextTypography>
              </NavLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
