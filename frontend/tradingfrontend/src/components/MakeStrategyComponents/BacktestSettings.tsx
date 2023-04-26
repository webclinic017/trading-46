import * as React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import { StrategyContext } from '../MakeStrategyContext/StrategyContext';
import { Types } from '../MakeStrategyContext/StategyReducers';
import { v4 as uuidv4 } from 'uuid';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef, useEffect, useState, useContext } from 'react';
import NativeSelect from '@mui/material/NativeSelect';

import axios from 'axios';
export default function BacktestSettings() {
  //以下為暫時用來測試的資料
  async function login(username, password) {
    const data = {
      email: username,
      password: password,
    };
    await axios
      .post('http://localhost:8050/api/v1/auth/login', data)
      .then((response) => {
        console.log(response.data);
        localStorage.setItem('access_token', response.data.access_token);
      })
      .catch((error) => {
        console.log(error);
      });
  }
  useEffect(() => {
    login('test01@example.com', '123456');
  }, []);
  const [all_data, setAll_data] = useState({
    stock_symbol: '2033',
    strategy_id: '6440e166e21de61de0e59e50',
    buy_strategy:
      'self.buy_pct = 0.5ChangeLine                self.sell_pct = 1',
    sell_strategy:
      'if backtesting.lib.crossover(self.ma10, self.ma20): self.buy()ChangeLine                elif backtesting.lib.crossover(self.ma20, self.ma10): self.sell()',
    plot: 'true',
    start_date: '2020-01-05',
    end_date: '2023-02-18',
    cash: '10000000',
    commission: '0.00145',
  });
  useEffect(() => {
    console.log(all_data);
  }, [all_data]);
  let isTrueSet = all_data.plot === 'true';
  const [response, setResponse] = useState('');
  async function single_test_with_custom_strategy() {
    const data = {
      stock_symbol: all_data.stock_symbol,
      strategy_id: all_data.strategy_id,
      buy_strategy: all_data.buy_strategy,
      sellstrategy: all_data.sell_strategy,
      plot: isTrueSet,
      start_date: all_data.start_date,
      end_date: all_data.end_date,
      cash: parseFloat(all_data.cash),
      commission: parseFloat(all_data.commission),
    };
    console.log(data);
    const config = {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
      },
    };

    await axios
      .post(
        'http://localhost:8050/api/v1/backtest/single_backtesting_with_custom_strategy',
        data,
        config
      )
      .then((response) => {
        console.log(response.data);
        setResponse(response.data.date);
      })
      .catch((error) => {
        console.log(error);
      });
  }
  // http://localhost:4041/htmlplots/test01@example.com_asd_2330.html
  let backtest_str = `http://localhost:4041/htmlplots/test01@example.com_asd_${all_data.stock_symbol}.html`;
  console.log(backtest_str);
  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        <Card sx={{ display: 'flex' }}>
          <Box sx={{ display: 'flex', flexDirection: 'column' }}>
            <Stack direction="row" spacing={1}>
              <TextField
                id="outlined-multiline-flexible"
                label="stock_symbol"
                multiline
                InputLabelProps={{
                  shrink: true,
                }}
                value={all_data.stock_symbol}
                onChange={(e) =>
                  setAll_data({ ...all_data, stock_symbol: e.target.value })
                }
              ></TextField>
              <TextField
                id="outlined-multiline-flexible"
                label="strategy_id"
                multiline
                InputLabelProps={{
                  shrink: true,
                }}
                value={all_data.strategy_id}
                onChange={(e) =>
                  setAll_data({ ...all_data, strategy_id: e.target.value })
                }
              ></TextField>
              <Box sx={{ minWidth: 120 }}>
                <FormControl fullWidth>
                  <InputLabel variant="standard" htmlFor="uncontrolled-native">
                    plot
                  </InputLabel>
                  <NativeSelect
                    defaultValue={30}
                    inputProps={{
                      name: 'age',
                      id: 'uncontrolled-native',
                    }}
                    onChange={(e) =>
                      setAll_data({ ...all_data, plot: e.target.value })
                    }
                  >
                    <option value={'true'}>True</option>
                    <option value={'false'}>False</option>
                  </NativeSelect>
                </FormControl>
              </Box>
            </Stack>
            <Stack direction="row" spacing={1}>
              <TextField
                id="outlined-multiline-flexible"
                label="start_date"
                multiline
                InputLabelProps={{
                  shrink: true,
                }}
                value={all_data.start_date}
                onChange={(e) =>
                  setAll_data({ ...all_data, start_date: e.target.value })
                }
              ></TextField>
              <TextField
                id="outlined-multiline-flexible"
                label="end_date"
                multiline
                value={all_data.end_date}
                InputLabelProps={{
                  shrink: true,
                }}
                onChange={(e) =>
                  setAll_data({ ...all_data, end_date: e.target.value })
                }
              ></TextField>
              <TextField
                id="outlined-multiline-flexible"
                label="cash"
                multiline
                InputLabelProps={{
                  shrink: true,
                }}
                value={all_data.cash}
                onChange={(e) =>
                  setAll_data({ ...all_data, cash: e.target.value })
                }
              ></TextField>
              <TextField
                id="outlined-multiline-flexible"
                label="commission"
                multiline
                InputLabelProps={{
                  shrink: true,
                }}
                value={all_data.commission}
                onChange={(e) =>
                  setAll_data({ ...all_data, commission: e.target.value })
                }
              ></TextField>
            </Stack>
            {response}
            {/* <iframe title="cool" src={backtest_str} width="700px" height="500px"></iframe> */}
          </Box>
          <Button>單策略回測</Button>
        </Card>
      </Box>
    </>
  );
}