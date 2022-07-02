import './App.css';
import MidSection from './components/MidSection';
import LeftSection from './components/LeftSection';
import RightSection from './components/RightSection';

const EMPLOYEE = "http://localhost:8000/api/employees/";



function App() {
  return (
    <main className="App">
      <div className="container">
        <LeftSection />
        <MidSection />
        <RightSection />
      </div>
    </main>
  );
}

export default App;
