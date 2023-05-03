import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useRef, useEffect, useState, useContext } from 'react';
import MakeStrategyBoard from 'src/components/MakeStrategyComponents/MakeStrategyBoard';
import SelectStrategy from 'src/components/MakeStrategyViewer/SelectStrategy';
import { SortableItem } from './SortableItemS';
import Container from 'react-bootstrap/Container';
import Stack from '@mui/material/Stack';
import BoardSectionList from 'src/components/dndComponents/BoardSectionList';
import DisplayBacktestingHtml from 'src/components/MakeStrategyComponents/DisplayBacktestingHtml';
import BacktestSettings from 'src/components/MakeStrategyComponents/BacktestSettings';
import SelectStrategySelectBar from 'src/components/MakeStrategyComponents/SelectStrategySelectBar';
import { DndContext, closestCenter } from '@dnd-kit/core';
import { StrategyContext } from 'src/components/MakeStrategyContext/StrategyContext';

import {
  arrayMove,
  SortableContext,
  verticalListSortingStrategy,
} from '@dnd-kit/sortable';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
  overflow: 'hidden',
}));

export default function MakeStrategy() {
  const { state, dispatch } = React.useContext(StrategyContext);
  const windowSize = useRef([window.innerWidth, window.innerHeight]);
  let leftPixel = windowSize.current[0] > 1440 ? '312px' : '84px';
  const [languages, setLanguages] = useState([
    'JavaScript',
    'Python',
    'TypeScript',
  ]);
  function handleDragEnd(event) {
    console.log('Drag end called');
    const { active, over } = event;
    console.log('ACTIVE: ' + active.id);
    console.log('OVER :' + over.id);

    if (active.id !== over.id) {
      setLanguages((items) => {
        const activeIndex = items.indexOf(active.id);
        const overIndex = items.indexOf(over.id);
        console.log(arrayMove(items, activeIndex, overIndex));
        return arrayMove(items, activeIndex, overIndex);
        // items: [2, 3, 1]   0  -> 2
        // [1, 2, 3] oldIndex: 0 newIndex: 2  -> [2, 3, 1]
      });
    }
  }

  //     <DndContext
  //     collisionDetection={closestCenter}
  //     onDragEnd={handleDragEnd}
  // >
  //     <Container className="p-3" style={{ "width": "50%" }} align="center">
  //         <h3>The best programming languages!</h3>
  //         <SortableContext
  //             items={languages}
  //             strategy={verticalListSortingStrategy}
  //         >
  //             {/* We need components that use the useSortable hook */}
  //             {languages.map(language => <SortableItem key={language} id={language} />)}
  //         </SortableContext>
  //     </Container>
  // </DndContext>
  return (
    <Box
      sx={{
        flexGrow: 1,
        position: 'absolute',
        right: '12px',
        top: '64px',
        left: '84px',
      }}
    >
      {state?.SingleBacktest.length !== 0 ?
        <Grid container spacing={2}>
          <Grid item xs={6} md={6}>
            <Stack spacing={2} direction="column">
              <Item>單一個股回測</Item>
              <Item>
                <SelectStrategySelectBar/>
              </Item>
              <Item>
                <MakeStrategyBoard />
              </Item>
              {/* <Item>
              <BacktestSettings />
            </Item> */}
            </Stack>
          </Grid>
          <Grid item xs={6} md={6} xl={6} lg={6}>
            <Item style={{ minHeight: '500px' }}>
              <DisplayBacktestingHtml />
            </Item>
            {/* <BoardSectionList /> */}
          </Grid>
        </Grid> : <Grid container spacing={2}>
          <Grid item xs={6} md={6}>
            <Item><SelectStrategy /></Item>
          </Grid>
        </Grid>}
    </Box>
  );
}
