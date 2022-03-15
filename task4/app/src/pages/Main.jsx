import { useState, useEffect } from 'react';
import './Main.css';
import axios from 'axios';

function Main() {

  const [response, setResponse] = useState("");
  
  function getApiCall() {
    axios.get(`http://127.0.0.1:8081/`).then(res => {
      setResponse(res.data);
      console.log(res.data);
    });
  }

  useEffect(() => {
    getApiCall();
  }, []);

  return (
    <div className="Main">
        <p>{response}</p>
    </div>
  );
}
export default Main;
