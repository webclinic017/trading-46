import styled from 'styled-components';

import NxWelcome from './nx-welcome';
import Dndpage from '../pages/Dndpage';
import Backtest from '../pages/Backtest';
const StyledApp = styled.div`
  // Your style here
`;

export function App() {
  return (
    <StyledApp>
      <Backtest></Backtest>
      {/* <Dndpage></Dndpage> */}
      {/* <NxWelcome title="tradingfrontend" /> */}
    </StyledApp>
  );
}

export default App;
