import * as React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import { StrategyContext } from '../MakeStrategyContext/StrategyContext';
import {
  Types,
  BacktestTypes,
  StrategyTypes,
} from '../MakeStrategyContext/StategyReducers';
export default function ConditionAddList(props: any) {
  function IndividualIndicators(props: any) {
    // id: uuidv4(),
    // category:"standard",
    // type:'live',
    // indicator_1 :'id1',
    // compare_operator:'>',
    // indicator_2 :'id2',
    // buyOrSell:'buy',
    // amount:0,
    // unit:'percent',
    const { state, dispatch } = React.useContext(StrategyContext);


    const [comparsionOperator, setComparsionOperator] = React.useState(
      props.indicator?.compare_operator
    );
    const [selectedIindicator1, setSelectedIindicator1] = React.useState(
      props.indicator?.indicator_1
    );
    const [selectedIindicator2, setSelectedIindicator2] = React.useState(
      props.indicator?.indicator_2
    );
    const [buyOrSell, setBuyOrSell] = React.useState(
      props.indicator?.buyOrSell
    );
    const [buySellAmount, setBuySellAmount] = React.useState(
      props.indicator?.amount
    );
    const [compareMode, setCompareMode] = React.useState(true);
    const handleOperatorChange = (event: SelectChangeEvent) => {
      console.log(event.target.value);
      setComparsionOperator(event.target.value);
      console.log(comparsionOperator);
    };
    const handleIindicator1Change = (event: SelectChangeEvent) => {
      console.log(event.target.value, 'selectedIindicator');
      setSelectedIindicator1(event.target.value);
      console.log(selectedIindicator, 'selectedIindicator');
    };
    const handleIindicator2Change = (event: SelectChangeEvent) => {
      console.log(event.target.value, 'selectedIindicator');
      setSelectedIindicator2(event.target.value);
      console.log(selectedIindicator, 'selectedIindicator');
    };
    const handleBuyOrSellChange = (event: SelectChangeEvent) => {
      console.log(event.target.value, 'BuyOrSellChange');
      setBuyOrSell(event.target.value);
      console.log(buyOrSell, 'BuyOrSellChange');
    };
    const handleBuySellAmountChange = (event: SelectChangeEvent) => {
      console.log(event.target.value, 'BuySellAmountChange');
      setBuySellAmount(event.target.value);
      console.log(buySellAmount, 'BuySellAmountChange');
      // props.updateIndicatorList(props.index, props.indicator[0], comparsionOperator, selectedIindicator, buyOrSell, event.target.value)
    };
    const handleCompareMode = () => {
      setCompareMode(!compareMode);
    };
    const handleChange = (event: SelectChangeEvent) => {
      setAge(event.target.value as string);
    };
    const handleClose = () => {
      setAge('');
    };
    const handleDeleteIndex = () => {
      console.log(props?.indicator);
      console.log(props?.index);
      removeIindicatorList(props.index);
    };
    // const handleSendUpdatedBuyCondition = () => {
    //   dispatch({
    //     Type: StrategyTypes.UPDATE_BUY_INDICATOR
    //     paylaod: {
    //       id: props.index,
    //       cate
    //   })
    return (
      <Box sx={{ minWidth: 120 }}>
        <Stack direction="row" spacing={1}>
          <Button variant="contained" onClick={handleCompareMode}>
            切換
          </Button>
          <FormControl sx={{ m: 1, minWidth: 120 }}>
            <InputLabel id="demo-simple-select-label">初始指標</InputLabel>
            <Select
              autoWidth
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={selectedIindicator1}
              label="Age"
              onChange={handleIindicator1Change}
            >
              {/* {props.selectedFactors.map((factor) => {
                  return <MenuItem value={factor}>{factor}</MenuItem>;
                })} */}
            </Select>
          </FormControl>
          <FormControl sx={{ m: 1, minWidth: 50 }} fullWidth>
            <InputLabel id="demo-simple-select-label">比較運算</InputLabel>
            <Select
              autoWidth
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={comparsionOperator}
              label="比較"
              onChange={handleOperatorChange}
            >
              <MenuItem value={'<'}>小於</MenuItem>
              <MenuItem value={'>'}>大於</MenuItem>
              {/* <MenuItem value={"<="}>小於等於</MenuItem>
                            <MenuItem value={">="}>大於等於</MenuItem>
                            <MenuItem value={"=="}>等於</MenuItem> */}
            </Select>
          </FormControl>
          {compareMode ? (
            <FormControl sx={{ m: 1, minWidth: 120 }}>
              <InputLabel id="demo-simple-select-label">比較指標</InputLabel>
              <Select
                autoWidth
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={selectedIindicator2}
                label="Age"
                onChange={handleIindicator2Change}
              >
                {/* {props.selectedFactors.map((factor) => {
                  return <MenuItem value={factor}>{factor}</MenuItem>;
                })} */}
              </Select>
            </FormControl>
          ) : (
            <TextField
              sx={{ m: 1, minWidth: 120 }}
              InputLabelProps={{
                shrink: true,
              }}
              onChange={(e) => {
                handleIindicator2Change(e);
              }}
              value={selectedIindicator2}
              id="outlined-basic"
              label="數值"
              variant="outlined"
            />
          )}
          {/* <FormControl sx={{ m: 1, minWidth: 120 }}>
            <InputLabel id="demo-simple-select-label">買或賣</InputLabel>
            <Select
              autoWidth
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={buyOrSell}
              label="買賣"
              onChange={handleBuyOrSellChange}
            >
              <MenuItem value={'or'}>單一條件</MenuItem>
              <MenuItem value={'and'}>共同條件</MenuItem>
              <MenuItem value={"<="}>小於等於</MenuItem>
                            <MenuItem value={">="}>大於等於</MenuItem>
                            <MenuItem value={"=="}>等於</MenuItem>
            </Select>
          </FormControl> */}
          <TextField
            sx={{ m: 1, minWidth: 120 }}
            InputLabelProps={{
              shrink: true,
            }}
            onChange={(e) => {
              handleBuySellAmountChange(e);
            }}
            value={buySellAmount}
            id="outlined-basic"
            label="數值"
            variant="outlined"
          />
          <Button variant="contained" onClick={handleDeleteIndex}>
            刪除
          </Button>
        </Stack>
      </Box>
    );
  }
  const { state, dispatch } = React.useContext(StrategyContext);
  const [factor, setFactor] = React.useState('');
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const [indicatorList, setIndicatorList] = React.useState([]);
  const open = Boolean(anchorEl);
  const handleSingleBacktestChild = () => {
    console.log(indicatorList);
  };
  const handleOpen = (event: React.MouseEvent<HTMLButtonElement>) => {
    // setIndicatorList([...indicatorList, <IndividualIndicators />])
    setAnchorEl(event.currentTarget);
  };
  const handleSetFactor = (factor) => {
    setFactor(factor.target.value);
  };
  const handleAddIndicatorList = () => {
    if (props.selectedFactors?.length > 0) {
      setIndicatorList([...indicatorList, [factor, '<', factor, '買入', 0]]);
      console.log(indicatorList);
      setAnchorEl(null);
    } else {
      alert('請先新增指標');
    }
  };
  const handleClose = (e) => {
    console.log(e.target.value);
    setAnchorEl(null);
  };

  // function removeItem(indexToRemove) {
  //     const newItems = [...items.slice(0, indexToRemove), ...items.slice(indexToRemove + 1)];
  //     setItems(newItems);
  //   }
  function removeIindicatorList(indexToRemove) {
    const newItems = [
      ...indicatorList.slice(0, indexToRemove),
      ...indicatorList.slice(indexToRemove + 1),
    ];
    setIndicatorList(newItems);
    console.log(indicatorList);
    console.log(indexToRemove);
  }

  function updateIndicatorList(
    index,
    indicator1,
    operator,
    indicator2,
    buyOrSell,
    buySellAmount
  ) {
    const newItems = [...indicatorList];
    console.log(index);
    console.log(indicatorList);
    console.log(newItems[index]);
    let coverArr = [indicator1, operator, indicator2, buyOrSell, buySellAmount];
    console.log(coverArr);
    newItems[index] = coverArr;
    console.log(newItems);
    setIndicatorList(newItems);
  }
  console.log(props.selectedFactors);
  // {indicatorList.map((indicator, index) => (
  //   <Box sx={{ width: '100%' }}>
  //     <IndividualIndicators
  //       indicatorList={indicatorList}
  //       selectedFactors={props.selectedFactors}
  //       indicator={indicator}
  //       index={index}
  //       removeIindicatorList={removeIindicatorList}
  //       updateIndicatorList={updateIndicatorList}
  //     />
  //   </Box>
  // ))}
  return (
    <div>
      <Box style={{ width: '100%' }}>
        <Stack direction="column" spacing={2}>
          <Box>
            <Stack direction="column" spacing={2}>
              <Box sx={{ width: '100%' }}>
                <Typography variant="h6" gutterBottom component="div">
                  符合全部條件
                </Typography>
                {state?.StategyTasks[0]?.strategy_code?.buy_signals.map((indicator, index) => {
                  if (indicator.type === "and") {
                    return (
                      <Box sx={{ width: '100%' }} key={index}>
                        <IndividualIndicators
                          // indicatorList={indicatorList}
                          // selectedFactors={props.selectedFactors}
                          indicator={indicator}
                          index={index}
                        // removeIindicatorList={removeIindicatorList}
                        // updateIndicatorList={updateIndicatorList}
                        />
                      </Box>
                    );
                  }
                  // return null; // 如果不是 '買入'，返回 null，即不渲染任何元素
                })}

                <Stack direction="column" spacing={1}>
                  {indicatorList.map((indicator, index) => (
                    <Box sx={{ width: '100%' }}>
                      <IndividualIndicators
                        indicatorList={indicatorList}
                        selectedFactors={props.selectedFactors}
                        indicator={indicator}
                        index={index}
                        removeIindicatorList={removeIindicatorList}
                        updateIndicatorList={updateIndicatorList}
                      />
                    </Box>
                  ))}
                </Stack>
                <Typography variant="h6" gutterBottom component="div">
                  符合部分條件
                </Typography>
                <Stack direction="column" spacing={1}>

                  {indicatorList.map((indicator, index) => (
                    <Box sx={{ width: '100%' }}>
                      <IndividualIndicators
                        indicatorList={indicatorList}
                        selectedFactors={props.selectedFactors}
                        indicator={indicator}
                        index={index}
                        removeIindicatorList={removeIindicatorList}
                        updateIndicatorList={updateIndicatorList}
                      />
                    </Box>
                  ))}
                </Stack>
                <Typography variant="h6" gutterBottom component="div">
                  符合即時條件
                </Typography>
                <Stack direction="column" spacing={2}>
                  {indicatorList.map((indicator, index) => (
                    <Box sx={{ width: '100%' }}>
                      <IndividualIndicators
                        indicatorList={indicatorList}
                        selectedFactors={props.selectedFactors}
                        indicator={indicator}
                        index={index}
                        removeIindicatorList={removeIindicatorList}
                        updateIndicatorList={updateIndicatorList}
                      />
                    </Box>
                  ))}
                </Stack>
              </Box>
            </Stack>
          </Box>
        </Stack>
      </Box>
      <Box sx={{ mb: 1 }}>
        <Button
          onClick={() => {
            handleSingleBacktestChild();
          }}
        >
          新增策略
        </Button>
        <Button
          onClick={() => {
            handleSingleBacktestChild();
          }}
        >
          及時回測
        </Button>
      </Box>
    </div>
  );
}
