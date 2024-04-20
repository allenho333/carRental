import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.less";
import axios from "axios";

function App() {
  const [display, setDisplay] = useState("");
  useEffect(() => {
    // axios.get("http://127.0.0.1:8000/api/").then((res) => {
    //   console.log(res.data);
    //   setDisplay(res.data);
    // });
    axios.post("http://127.0.0.1:7864/users/login",{
      "password": "string",
      "username": "string"
    }).then((res) => {
      console.log("login",res.data,res.data.data.data);
      setDisplay(res.data.data.data);
    });
    axios.post("http://127.0.0.1:7864/users/signup",{
      "password": "string",
      "username": "string"
    }).then((res) => {
      console.log("signup",res.data);
    });
  });
  return (
    <>
      this is hahaha
      <br />
      {display}
    </>
  );
}

export default App;
