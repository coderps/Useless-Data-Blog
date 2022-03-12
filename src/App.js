import "./App.css";
import Navigation from "./components/navigation";
import { BrowserRouter as Router } from "react-router-dom";

function App() {
  return (
    <div>
      <Router>
        <Navigation />
      </Router>
    </div>
  );
}

export default App;
