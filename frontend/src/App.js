import './App.css';
import axios from 'axios';

const EMPLOYEE = "http://localhost:8000/api/employees/";


// Register user
const employees = async () => {
	const response = await axios.get(EMPLOYEE);
	return response.data;
};

function App() {
  return (
    <div className="App">
        Home Page
    </div>
  );
}
console.log(employees());

export default App;
