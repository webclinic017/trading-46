import { Typography } from '@material-ui/core';
// import { Switch } from "react-router";
// import { BrowserRouter as Router } from 'react-router-dom';
// 修飾輸入框套件
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
//勾選記住帳號資訊套件
// import Checkbox from '@material-ui/core/Checkbox';
//按鈕
import Button from '@material-ui/core/Button';
import { createTheme, ThemeProvider } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import { makeStyles, withStyles } from '@material-ui/styles';
//login套件
import axios from 'axios';
import { useFormik } from "formik";
import React, { useState } from 'react';
//頁面跳轉
// import { useLocation } from 'react-router';
import {
  NavLink,
  // Link, Route,
  useHistory
} from 'react-router-dom';
import * as yup from "yup";
import * as Constant from '../components/Constant';
import "../css/All.css";
import Imagewelcome from "../components/Images/ImageWelcome.png";







const CssTextField = withStyles({
  root: {
    // '& label.Mui-focused': {
    //   color: '#2C82FF',
    // },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'green',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        
        borderRadius: `8px 8px 8px 8px`,
        border:'1px,solid',
        boxShadow: '0px 4px 10px rgba(25, 1, 52, 0.16)',
        borderColor: '#CFCFCF',
      },
      '&:hover fieldset': 
      {
        border:'10px,solid',
        backgroundColor: 'none',
        borderColor:'#5D5D5D',
        boxShadow: '0px 4px 10px rgba(25, 1, 52, 0.16)',
      },
      '&.Mui-focused fieldset': 
      {
        borderColor: '#0957C3',
        backgroundColor: 'none',
      },
      '&:error fieldset':{
        borderColor:'#ff0000',

      }
    },
  },
})(TextField);
//輸入欄顏色



// const login = () => {
//     const request = 
//       {url: Constant.AUTH_API_NODE + '/login'}
//     axios({
//       method:'post',
//       url:request.url,
//       data:{
//         "email":Data.email,
//         "password":Data.password
//       },
//     })
//     .then((response)=>{

//       //console.log(response)

//       return response

//     })
//     .then((data)=>{
//       const statuscode = data.statusText
      
//       //console.log(statuscode)
//       //console.log('data',data)
//       return data
    
//     })




//     .catch((err) => { 
      
//       if (err="401") {
//         setErrormessage(
//           "你輸入錯了" 
//         );
//       }
//       else if(err="none"){
//         setErrormessage(
//           ""
//         );
//       }
//       return err
//       console.error(err) })
//   }

function App() {
  
  //checkbox
  
  const BlackTextTypography = withStyles({
    root: {
      color: "#5D5D5D",
      fontSize: "14px",
      fontFamily:[
        'Noto Sans CJK TC',
      ].join(','),
    },
  })(Typography);
  
  
  
  //按鈕顏色
  const BootstrapButtonlogin = withStyles({
    root: {
      boxShadow: 'none',
      width: '184px',
      height: '48px',
      textTransform: 'none',
      fontSize: 18,
      padding: '0px 0px',
      border: '1px solid',
      lineHeight: 1.5,
      backgroundColor: '#0957C3',
      borderColor: 'none',
      fontFamily: [
        'Noto Sans CJK TC',
      ].join(','),
      '&:hover': {
        borderColor: '#307FE2',
        boxShadow: 'none',
        backgroundColor: '#307FE2',
      },
      '&:active': {
        boxShadow: 'none',
        backgroundColor: '#0957C3',
        borderColor: '#0957C3',
      },
      '&:focus': {
        boxShadow: '0 0 0 0.2rem ',
      },
      '&:disabled':{
        color:'#E4E3E2',
        backgroundColor: '#0957C3',
      }
    },
  })(Button);
  
  const useClasses = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
    },
    textField: {
      height: '55px',
      width: '400px',
      borderRadius: `8px 8px 8px 8px`,
      padding: '0px, 0px, 0px, 0px',
      borderColor:'#0957C3',
      backgroundColor:'#fff',
      boxShadow: '0px 4px 10px rgba(25, 1, 52, 0.16)',
      '&:hover': {
        border:'3px,solid',
        backgroundColor: 'none',
        borderColor:'#5D5D5D',
        boxShadow: '0px 4px 10px rgba(25, 1, 52, 0.16)',
      },
      '&:active': {
        borderColor: '#fff',
        backgroundColor:'none',

      },
      '&:focus': {
        borderColor: '#fff',
        color:'none',
        backgroundColor:'none',
      },
      
    },
    helperText:{
      color:'#ff0000',
    },
    label:{
      fontFamily:[
        'Noto Sans CJK TC',
      ],
    }
  }));
  const classes = useClasses()

  // Theme顏色
  const theme = createTheme({
    palette: {
      primary: {
        main: '#0957C3',
        dark: '#002884',},
      secondary:{main: '#307FE2',},
    },
    typography: {
      "fontFamily":  'Noto Sans CJK TC',
     }
  });
  
  





  //loginreturn



  


  


  const validationSchema = yup.object({
    email: yup.string().required("電子郵件是必填欄位"),
    password: yup.string().required("密碼是必填欄位"),
  });
  
  
    // const { switchToSignup } = useContext(AccountContext);

    const [errorcode, setErrorcode] = useState(false);
 
    const onSubmit = async (values) => {

      const response = await axios
        .post(Constant.AUTH_API_NODE + '/login', values)
        .catch((err) => {
          if (err && err.response ==="401") 

          setErrorcode(true);

          //console.log(response)
        });
  
      if (response) {
        history.push("/loading")
        // alert("Welcome back in. Authenticating...");
        //console.log(response)
      }
    };
  
    const formik = useFormik({
      initialValues: { email: "", password: "" },
      validateOnBlur: true,
      onSubmit,
      validationSchema: validationSchema,
    });



  const history = useHistory();

  

  return (
    <div className="mainscreen">
      <img className="layoutLeft" src={Imagewelcome} alt="" />
      <div className="layoutRight">
        <div className="infoForgetPassword">
          <div className="lebel_Title h2 heavy">無人機橋梁檢測系統(DBIS) </div>
          <div className="lebelhint h6 regular">
            如遺忘密碼，可透過註冊電子郵件重新設置。
          </div>

          <div className="enterColumn1">
            <ThemeProvider theme={theme}>
              <CssTextField
                name="email"
                id="input"
                label="請輸入電子郵件"
                value={formik.values.email}
                type="input"
                className={classes.textField}
                onChange={formik.handleChange}
                autoComplete="current-password"
                variant="outlined"
                helperText={
                  formik.touched.email && formik.errors.email
                    ? formik.errors.email
                    : ""
                }
                onBlur={formik.handleBlur}
                error={errorcode}
                InputLabelProps={{
                  className: classes.label,
                }}
                FormHelperTextProps={{
                  className: classes.helperText,
                }}
              />
            </ThemeProvider>
          </div>

          <div className="buttonsForgetPassword">
            <BootstrapButtonlogin
              variant="contained"
              color="primary"
              disableRipple
              className="buttonsForgetPassword"
              onClick={() => history.push("/ChangePassword")}
            >
              重新設置密碼
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
  );
}

export default App;
