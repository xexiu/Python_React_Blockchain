import logo from '../assets/logo.png';
// import Joke from './Joke';
import Blockchain from './Blockchain';
import WalletInfo from './WalletInfo';

function App(): JSX.Element {
  // useState() // <-- return an array with 2 values

  // const state = useState('')
  // const useQuery = state[0];
  // const setUseQuery = state[1];

  return (
    <div className='APP'>
      <img src={logo} alt='application-logo' className='logo' />
      <h3>Welcome to pychain</h3>
      <br />
      <WalletInfo />
      <br />
      <Blockchain />
    </div>
  );
}

export default App;
