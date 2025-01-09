import React, { useEffect, useState } from "react";
import { fetchTickers, addTicker } from ".";
import withData from "../../components/hoc/withData.jsx";
import ActionToggle from "../../components/ActionToggle.jsx";

const Tickers = ({ data }) => {
  const [ticker, setTicker] = useState("");

  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div className="flex flex-row h-full mx-4 md:mx-16 my-20">
      <div className="flex flex-col w-1/2 bg-slate text-slate p-4 ml-4">
      <h1 className="text-3xl font-semibold">Ticker list</h1>
        <h3 className="text-lg opacity-75 italic my-2 mb-4">
          Toggle/untoggle the tickers to stop automatic tracking
        </h3>
        {data.tickers && data.tickers.length > 0
          ? data.tickers.map((t) => (
              <div className="flex flex-row items-center my-1" key={t.ticker}>
                <div className="mr-4 w-16">{t.ticker}</div>
                <ActionToggle
                  initialState={t.keepTracking}
                  onChange={(newState) => {
                    console.log(`${t.ticker} toggle changed to: ${newState}`);
                  }}
                />
              </div>
            ))
          : "No tickers available"}
      </div>

      <div className="flex flex-col w-1/2 p-4">
        <h1 className="text-3xl font-semibold">Add a ticker to track</h1>
        <h3 className="text-lg opacity-75 italic my-2 mb-4">
          Add a ticker from any stock exchange to track the gamma and delta
          exposure
        </h3>
        <form className="flex flex-col items-start">
          <label className="text-sm">Ticker</label>
          <input
            className="border border-black my-2"
            id="ticker"
            value={ticker}
            onChange={(event) => setTicker(event.target.value)}
            type="text"
          />
          <button type="button" onClick={() => addTicker(ticker)}>
            Button
          </button>
        </form>
      </div>
    </div>
  );
};

export default withData(Tickers, fetchTickers);
