import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef } from 'react';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
  overflow: 'hidden',
}));

export default function SingleBacktest() {
  const windowSize = useRef([window.innerWidth, window.innerHeight]);
  let leftPixel = windowSize.current[0] > 1440 ? '312px':'84px'
  console.log(leftPixel)
  console.log(windowSize.current[0])
  return (
    <Box sx={{ flexGrow: 1, position:'absolute' , right:"12px", top:'64px', left:leftPixel}}>
      <Grid container spacing={2}>
        <Grid item xs={6} md={9}>
          <Item>xs=6 md=8</Item>
        </Grid>
        <Grid item xs={6} md={3}>
          <Item>xs=6 md=4 </Item>
        </Grid>
        <Grid item xs={6} md={6}>
          <Item>xs=6 md=4</Item>
        </Grid>
        <Grid item xs={6} md={6}>
          <Item>xs=6 md=8</Item>
        </Grid>
      </Grid>
    </Box>
  );
}