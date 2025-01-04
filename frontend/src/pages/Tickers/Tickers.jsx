import React, { useEffect, useState } from "react";
import { fetchTickers, addTicker } from ".";
import withData from "../../components/hoc/withData.jsx";

const Tickers = ({ data }) => {
  const [ticker, setTicker] = useState("");


  if (!data) {
    return <div>Loading...</div>;
  }

  console.log(data.tickers)
  
  return (
    <>
      <div className="flex flex-grow bg-slate text-slate">
        {data.tickers && data.tickers.length > 0
          ? data.tickers.map((t, index) => 
          <div className="flex flex-col">
            <div>{t.ticker}</div>
            <input type="checkbox"/>
          </div>)
          : "No tickers available"}
      </div>
      <form>
        <label>Ticker</label>
        <input
          id="ticker"
          value={ticker}
          onChange={(event) => setTicker(event.target.value)}
          type="text"
        />
        <button type="button" onClick={() => addTicker(ticker)}>
          Button
        </button>
      </form>
    </>
  );
};

export default withData(Tickers, fetchTickers);
