import './App.css';
import PersonalCard from './components/PersonalCard';

const EMPLOYEE = "http://localhost:8000/api/employees/";



function App() {
  return (
    <div className="App">
      <PersonalCard />
    </div>
  );
}

export default App;
