import React, { useEffect, useState } from "react";
import { fetchTickers, addTicker } from ".";
import withData from "../../components/hoc/withData.jsx";
import ActionToggle from "../../components/ActionToggle.jsx";
import useTickers from "../../hooks/useTickers.jsx"

const Tickers = ({ data }) => {
  const [ticker, setTicker] = useState("");
  const { tickers, addNewTicker, error } = useTickers(data);

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
        {tickers && tickers.length > 0
          ? tickers.map((t) => (
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
          : <div>No tickers available</div>}
      </div>

      <div className="flex flex-col w-1/2 p-4">
        <h1 className="text-3xl font-semibold">Add a ticker to track</h1>
        <h3 className="text-lg opacity-75 italic my-2 mb-4">
          Add a ticker from any stock exchange to track the gamma and delta exposure
        </h3>
        <form className="flex flex-col items-start">
          {error && <div className="text-red-500 mb-2">{error}</div>}
          <label className="text-base">Ticker</label>
          <input
            className="border border-black my-2 p-1"
            id="ticker"
            value={ticker}
            onChange={(event) => setTicker(event.target.value)}
            type="text"
          />
          <button
            className="px-2 py-1 rounded-md border bg-cyan-700"
            type="button"
            onClick={async () => {
              if (!ticker.trim()) {
                console.error("Ticker cannot be empty.");
                return;
              }
              try {
                await addNewTicker(ticker);
                setTicker("");
              } catch (error) {
                console.error("Failed to add ticker:", error);
              }
            }}
          >
            Save
          </button>
        </form>
      </div>
    </div>
  );
};

export default withData(Tickers, fetchTickers);