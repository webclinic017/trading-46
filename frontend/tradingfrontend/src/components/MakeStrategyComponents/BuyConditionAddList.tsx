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
import Chip from '@mui/material/Chip';

import {
  Types,
  BacktestTypes,
  StrategyTypes,
} from '../MakeStrategyContext/StategyReducers';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import { Card } from '@mui/material';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import { v4 as uuidv4 } from 'uuid';
export default function BuyConditionAddList(props: any) {
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

    const [openEdit, setOpenEdit] = React.useState(false);
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
    const handleCompareMode  =()=>{
      setCompareMode(!compareMode)
    }
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
    const [openTempIndicatorSelecetPanel, setOpenTempIndicatorSelecetPanel] = React.useState({
      panelAnd: false, panelOr: false, panelLive: false
    });
    const handleTempIndicatorSelecetPanelAnd = () => {
      setOpenTempIndicatorSelecetPanel({ ...openTempIndicatorSelecetPanel, panelAnd: !openTempIndicatorSelecetPanel.panelAnd });
    };
    const handleTempIndicatorSelecetPanelOr = () => {
      setOpenTempIndicatorSelecetPanel({ ...openTempIndicatorSelecetPanel, panelOr: !openTempIndicatorSelecetPanel.panelOr });
    };
    const [TempIndicatorSelecetPanelValue, setTempIndicatorSelecetPanelValue] = React.useState('1');

    const handleTempIndicatorSelecetPanelValueChange = (event: React.SyntheticEvent, newValue: string) => {
      setTempIndicatorSelecetPanelValue(newValue);
    };

    const handleTempIndicator1SelecetPanel = (e) => {
      setSelectedIindicator1(e.target.value)
      setOpenTempIndicatorSelecetPanel({ ...openTempIndicatorSelecetPanel, panelAnd: false });
    }

    const handleTempIndicator2SelecetPanel = (e) => {
      setSelectedIindicator2(e.target.value)
      setOpenTempIndicatorSelecetPanel({ ...openTempIndicatorSelecetPanel, panelOr: false });
    }
    const itemData = ["Open", "High", "Low", "Close", "Volume", "slowkd",",macd","RSI"]
    const handleOpenEdit = () => {
      setOpenEdit(!openEdit);
    };
    const handleCompleteEdit = () => {
      dispatch({
        type: StrategyTypes.UPDATE_BUY_INDICATOR,
        payload: {
          strategy_id: props.strategy_id,
          buy_and_indicator: {
            id: props.indicator.id,
            category: props.indicator.category,
            type: props.indicator.type,
            indicator_1: selectedIindicator1,
            compare_operator: comparsionOperator,
            indicator_2: selectedIindicator2,
            buyOrSell: props.indicator.buyOrSell,
            amount: buySellAmount,
            unit: props.indicator.unit,
          }
        },
      });
      console.log(state);
    };
    const handleDelete = () => {
      dispatch({
        type: StrategyTypes.DELETE_BUY_INDICATOR,
        payload: {
          strategy_id: props.strategy_id,
          buy_and_indicator: {
            id: props.indicator.id,
          }
        },
      });
      console.log(state);
    };


    return (
      <Box sx={{ minWidth: 120 }}>

        {openEdit ? (
          <Stack direction="row" spacing={1}>
            {/* <Button variant="contained" onClick={handleCompareMode}>
            切換
          </Button> */}
            <Button
              variant="outlined"
              id="demo-positioned-button"
              aria-controls={open ? 'demo-positioned-menu' : undefined}
              aria-haspopup="true"
              aria-expanded={open ? 'true' : undefined}
              onClick={handleTempIndicatorSelecetPanelAnd}
            >
              {selectedIindicator1}


            </Button>

            {/* <FormControl sx={{ m: 1, minWidth: 120 }}>
            <InputLabel id="demo-simple-select-label">初始指標</InputLabel>
            <Select
              autoWidth
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={selectedIindicator1}
              label="Age"
              onChange={handleIindicator1Change}
              onClick={handleTempIndicatorSelecetPanelAnd}
            >
              {openTempIndicatorSelecetPanel.panelAnd}
              <MenuItem value={selectedIindicator1}>{selectedIindicator1}</MenuItem>

              {props.selectedFactors.map((factor) => {
                  return <MenuItem value={factor}>{factor}</MenuItem>;
                })}
            </Select>
          </FormControl> */}

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
              <Button
                variant="outlined"
                id="demo-positioned-button"
                aria-controls={open ? 'demo-positioned-menu' : undefined}
                aria-haspopup="true"
                aria-expanded={open ? 'true' : undefined}
                onClick={handleTempIndicatorSelecetPanelOr}
              >
                {selectedIindicator2}
              </Button>
              // <FormControl sx={{ m: 1, minWidth: 120 }}>
              //   <InputLabel id="demo-simple-select-label">比較指標</InputLabel>
              //   <Select
              //     autoWidth
              //     labelId="demo-simple-select-label"
              //     id="demo-simple-select"
              //     value={selectedIindicator2}
              //     label="Age"
              //     onChange={handleIindicator2Change}
              //   >
              //     {/* {props.selectedFactors.map((factor) => {
              //       return <MenuItem value={factor}>{factor}</MenuItem>;
              //     })} */}
              //   </Select>
              // </FormControl>
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
              label="要售出的%數"
              variant="outlined"
            />
                      <Button variant="contained" onClick={handleCompareMode}>
            切換 {compareMode ? '數值' : '指標'}
          </Button>
            <Button
              variant="contained"
              id="demo-positioned-button"
              aria-controls={open ? 'demo-positioned-menu' : undefined}
              aria-haspopup="true"
              aria-expanded={open ? 'true' : undefined}
              onClick={handleCompleteEdit}
            >
              完成
            </Button>
            <Button variant="contained" onClick={handleDelete}>
              刪除
            </Button>
            {openTempIndicatorSelecetPanel.panelAnd ?
              <Card sx={{ overflow: 'auto', position: 'absolute', borderBottom: 1, borderColor: 'divider', zIndex: 10, width: '50%', height: '50%' }}>
                <TabContext value={TempIndicatorSelecetPanelValue}>
                  <Box >
                    <TabList variant="fullWidth" centered onChange={handleTempIndicatorSelecetPanelValueChange} aria-label="lab API tabs example">
                      <Tab label="技術指標" value="1" />
                      <Tab label="基本指標" value="2" />
                      <Tab label="籌碼指標" value="3" />
                    </TabList>
                  </Box>
                  <TabPanel
                    value="1">
                    <ImageList sx={{ width: '100%' }} cols={3} >
                      {itemData.map((item) => (
                        <ImageListItem key={item} >
                          <Button variant="contained" value={item} onClick={handleTempIndicator1SelecetPanel}>
                            {item}
                          </Button>
                        </ImageListItem>
                      ))}
                    </ImageList></TabPanel>
                  <TabPanel value="2">基本指標</TabPanel>
                  <TabPanel value="3">籌碼指標</TabPanel>
                </TabContext>
              </Card> : null
            }
            {openTempIndicatorSelecetPanel.panelOr ?
              <Card sx={{ overflow: 'auto', position: 'absolute', borderBottom: 1, borderColor: 'divider', zIndex: 10, width: '50%', height: '50%' }}>
                <TabContext value={TempIndicatorSelecetPanelValue}>
                  <Box >
                    <TabList variant="fullWidth" centered onChange={handleTempIndicatorSelecetPanelValueChange} aria-label="lab API tabs example">
                      <Tab label="技術指標" value="1" />
                      <Tab label="基本指標" value="2" />
                      <Tab label="籌碼指標" value="3" />
                    </TabList>
                  </Box>
                  <TabPanel
                    value="1">
                    <ImageList sx={{ width: '100%' }} cols={3} >
                      {itemData.map((item) => (
                        <ImageListItem key={item} >
                          <Button variant="contained" value={item} onClick={handleTempIndicator2SelecetPanel}>
                            {item}
                          </Button>
                        </ImageListItem>
                      ))}
                    </ImageList></TabPanel>
                  <TabPanel value="2">基本指標</TabPanel>
                  <TabPanel value="3">籌碼指標</TabPanel>
                </TabContext>
              </Card> : null
            }
          </Stack>) : (<Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Stack direction="row" spacing={1}>
              <Chip sx={{ width: "100px" }} label={selectedIindicator1} />
              <Chip sx={{ width: "50px" }} label={comparsionOperator} />
              <Chip sx={{ width: "100px" }} label={selectedIindicator2} />
              <Chip sx={{ width: "50px" }} label={buySellAmount} />
              <Button
                variant="outlined"
                id="demo-positioned-button"
                aria-controls={open ? 'demo-positioned-menu' : undefined}
                aria-haspopup="true"
                aria-expanded={open ? 'true' : undefined}
                onClick={handleOpenEdit}
              >
                編輯
              </Button>
            </Stack>
          </Box>
        )}
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
  let uuid = state?.StategyTasks[0]?.strategy_id
  const handleAddBuyAndIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'and',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyOrIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'or',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };
  const handleAddBuyLiveIndicator = () => {
    dispatch({
      type: StrategyTypes.ADD_BUY_INDICATOR,
      payload: {
        strategy_id: uuid,
        buy_and_indicator: {
          id: uuidv4(),
          category: "standard",
          type: 'live',
          indicator_1: 'id1',
          compare_operator: '>',
          indicator_2: 'id2',
          buyOrSell: 'buy',
          amount: 0,
          unit: 'percent',
        }
      },
    });
    console.log(state);
  };

  return (
    <div>
      <Box style={{ width: '100%' }}>
        <Stack direction="column" spacing={2}>
          <Box>
            <Stack direction="column" spacing={2}>
              <Box sx={{ width: '100%' }}>
                <Stack direction="row" spacing={2}>

                  <Typography variant="h6" gutterBottom component="div">
                    符合全部條件
                  </Typography>
                  <Button onClick={handleAddBuyAndIndicator}>增加條件</Button>
                </Stack>
                <Stack direction="column" spacing={2}>

                  {state?.StategyTasks[0]?.strategy_code?.buy_signals.map((indicator, index) => {
                    if (indicator.type === "and") {
                      return (

                        <Box sx={{ width: '100%' }} key={index}>
                          <IndividualIndicators
                            // indicatorList={indicatorList}
                            // selectedFactors={props.selectedFactors}
                            strategy_id={state?.StategyTasks[0]?.strategy_id}
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
                </Stack>

                <Stack direction="column" spacing={1}>

                </Stack>
                <Stack direction="row" spacing={2}>
                  <Typography variant="h6" gutterBottom component="div">
                    符合部分條件
                  </Typography>
                  <Button onClick={handleAddBuyOrIndicator}>增加條件</Button>
                </Stack>
                <Stack direction="column" spacing={1}>
                  {state?.StategyTasks[0]?.strategy_code?.buy_signals.map((indicator, index) => {
                    if (indicator.type === "or") {
                      return (

                        <Box sx={{ width: '100%' }} key={index}>
                          <IndividualIndicators
                            // indicatorList={indicatorList}
                            // selectedFactors={props.selectedFactors}
                            strategy_id={state?.StategyTasks[0]?.strategy_id}
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
                </Stack>
                <Stack direction="row" spacing={2}>

                  <Typography variant="h6" gutterBottom component="div">
                    符合即時條件
                  </Typography>
                  <Button onClick={handleAddBuyLiveIndicator}>增加條件</Button>
                </Stack>
                <Stack direction="column" spacing={2}>
                  {state?.StategyTasks[0]?.strategy_code?.buy_signals.map((indicator, index) => {
                    if (indicator.type === "live") {
                      return (

                        <Box sx={{ width: '100%' }} key={index}>
                          <IndividualIndicators
                            // indicatorList={indicatorList}
                            // selectedFactors={props.selectedFactors}
                            strategy_id={state?.StategyTasks[0]?.strategy_id}
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
                </Stack>
              </Box>
            </Stack>
          </Box>
        </Stack>
      </Box>
    </div>
  );
}
