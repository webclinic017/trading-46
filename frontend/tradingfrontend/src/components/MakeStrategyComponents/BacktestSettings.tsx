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
import { Types, BacktestTypes } from '../MakeStrategyContext/StrategyReducers';
import { v4 as uuidv4 } from 'uuid';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef, useEffect, useState, useContext } from 'react';
import { STATIC_SERVER_URL, STRATEGY_API, BACKTEST_API } from 'src/constants';
import NativeSelect from '@mui/material/NativeSelect';

import axios from 'axios';
export default function BacktestSettings() {
  const { state, dispatch } = React.useContext(StrategyContext);
  const [all_data, setAll_data] = useState({
    stock_symbol: state?.SingleBacktest[0]?.backtest_description?.stock_symbol,
    plot: "true",
    start_date: state?.SingleBacktest[0]?.backtest_description?.start_date,
    end_date: state?.SingleBacktest[0]?.backtest_description?.end_date,
    cash: state?.SingleBacktest[0]?.backtest_description?.cash,
    commission: state?.SingleBacktest[0]?.backtest_description?.commission,
  });
  let isTrueSet = all_data.plot === 'true';
  const [response, setResponse] = useState('');
  let useremail = localStorage.getItem('useremail');

  async function addStrategy() {
    const config = {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
      },
    };
    console.log(state?.SingleBacktest[0]?.backtest_strategy?.strategy_id)
    const data = {
      "id": state?.SingleBacktest[0]?.backtest_strategy?.strategy_id,
      "strategy_id": state?.SingleBacktest[0]?.backtest_strategy?.strategy_id,
      "strategy_name": state?.StrategyTasks[0]?.strategy_name,
      "strategy_description": "strategy_description",
      "strategy_code": {
        "init_indicators": [
          "KD",
          "MACD",
          "RSI",
          "SMA5"
        ],
        "stop_loss": 10,
        "take_profit": 20,
        "buy_first": true,
        "buy_signal": state?.StrategyTasks[0]?.strategy_code.buy_signal,
        "sell_signal": state?.StrategyTasks[0]?.strategy_code.sell_signal,
      },
      "strategy_type": "strategy_type",
      "strategy_parameters": "strategy_parameters",
      "strategy_author": useremail,
      "strategy_status": "strategy_status",
      "strategy_created_date": "2023-04-28T06:54:49.663336",
      "strategy_updated_date": "2023-04-28T06:54:49.663336",
    }
    await axios.post(`${STRATEGY_API}update_strategy_by_id`, data, config)
      .then((response) => {
        console.log(response.data);
      }
      ).catch((error) => {
        console.log(error);
      });
  };
  let backtest_str = `${STATIC_SERVER_URL}/htmlplots/${useremail}_${state.StrategyTasks[0].strategy_name}_${all_data.stock_symbol}.html`;
  async function single_test_with_custom_strategy() {
    addStrategy()

    const data = {
      stock_symbol: all_data.stock_symbol,
      strategy_id: state?.SingleBacktest[0]?.backtest_strategy?.strategy_id,
      // buy_strategy: state.,
      // sellstrategy: all_data.sell_strategy,
      plot: isTrueSet,
      start_date: all_data.start_date,
      end_date: all_data.end_date,
      cash: parseFloat(all_data.cash),
      commission: parseFloat(all_data.commission),
    };
    console.log(data);
    const config = {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
      },
    };

    await axios
      .post(
        `${BACKTEST_API}single_backtesting_with_custom_strategy`,
        data,
        config
      )
      .then((response) => {
        console.log(response);
        dispatch({
          type: BacktestTypes.UPDATE_BACKTEST_RESULT,
          payload: {
            backtest_id: state?.SingleBacktest[0]?.backtest_id,
            backtest_result: response.data.date
          },
        });
      })
      .catch((error) => {
        console.log(error);
      });
    dispatch({
      type: BacktestTypes.UPDATE_BACKTEST_HTML,
      payload: {
        backtest_id: state?.SingleBacktest[0]?.backtest_id,
        backtest_html: backtest_str,
      },
    });
    dispatch({
      type: BacktestTypes.UPDATE_BACKTEST_DESCRIPTION,
      payload: {
        backtest_id: state?.SingleBacktest[0]?.backtest_id,
        backtest_description: all_data,
      },
    });

  }
  // http://localhost:4041/htmlplots/test01@example.com_asd_2330.html
  console.log(backtest_str);

  return (

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
              placeholder='2033'
              onChange={(e) =>
                setAll_data({ ...all_data, stock_symbol: e.target.value })
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
              placeholder='2021-01-01'
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
              placeholder='2023-01-01'
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
              placeholder='1000000'
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
              placeholder='0.001425'
              InputLabelProps={{
                shrink: true,
              }}
              value={all_data.commission}
              onChange={(e) =>
                setAll_data({ ...all_data, commission: e.target.value })
              }
            ></TextField>
                    <Button onClick={single_test_with_custom_strategy}>單策略回測</Button>

          </Stack>
          {response}
          {state?.SingleBacktest[0]?.backtest_result ?

          <table>
            <thead>
              <tr>
                <th>Field</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
                { Object?.entries(JSON.parse(state?.SingleBacktest[0]?.backtest_result)).map(([key, value]) => (
                  <tr key={key}>
                    <td>{key}</td>
                    <td>{value}</td>
                  </tr>
                ))
               }
            </tbody>
          </table>
          :null}
          {/* <iframe title="cool" src={backtest_str} width="700px" height="500px"></iframe> */}
        </Box>
      </Card>
    </Box>

  );
}
