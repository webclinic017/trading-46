import styled from 'styled-components';

import NxWelcome from './nx-welcome';
import Dndpage from '../pages/Dndpage';
const StyledApp = styled.div`
  // Your style here
`;

export function App() {
  return (
    <StyledApp>
      <Dndpage></Dndpage>
      {/* <NxWelcome title="tradingfrontend" /> */}
    </StyledApp>
  );
}

export default App;
