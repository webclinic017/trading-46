import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef, useEffect, useState, useContext } from 'react';
import MakeStrategyBoard from 'src/components/MakeStrategyComponents/MakeStrategyBoard';
import { SortableItem } from '../../pages/SortableItemS';
import Container from 'react-bootstrap/Container';
import Stack from '@mui/material/Stack';
import {StrategyContext} from 'src/components/MakeStrategyContext/StrategyContext';
import {STRATEGY_API} from 'src/constants'
import axios from 'axios';

export default function SelectStrategy() {
    useEffect(() => {
        let config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('accessToken')}`,
                'Accept': 'application/json'
            }
        }
        axios.get(STRATEGY_API+'get_strategies_by_author',config).then((response) => {
            console.log(response.data);
            // dispatch({ type: 'SET_STRATEGY_TASKS', payload: response.data });
        });
    }, []);
    const { state, dispatch } = React.useContext(StrategyContext);

    return (
        <div >
            <h1> Select Strategies  {state?.StategyTasks[0]?.strategy_author}
            </h1>
            Select Strategies
        </div>
    )
}