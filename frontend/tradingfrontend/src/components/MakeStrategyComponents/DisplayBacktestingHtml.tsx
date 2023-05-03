import * as React from 'react';
import { styled } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import Chip from '@mui/material/Chip';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import ConditionAddList from '../../../../../legacyFile/ConditionAddListLegacy';
import { useState, useEffect, useContext } from 'react';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import NativeSelect from '@mui/material/NativeSelect';
import InputLabel from '@mui/material/InputLabel';
import axios from 'axios';
import { StrategyContext } from 'src/components/MakeStrategyContext/StrategyContext';
import { Types } from 'src/components/MakeStrategyContext/StategyReducers';
import { v4 as uuidv4 } from 'uuid';

export default function DisplayBacktestingHtml() {
    const { state, dispatch } = React.useContext(StrategyContext);

    return (
        <Box >
        {/* {state?.SingleBacktest[0]?.backtest_html} */}
            {/* <iframe title="cool" src="http://localhost:4041/htmlplots/test01@example.com_strategy_name_2033.html" width="100%" height="700px"></iframe> */}
            <iframe title="cool" src={state?.SingleBacktest[0]?.backtest_html} width="100%" height="700px"></iframe>
        </Box>
    )
}
