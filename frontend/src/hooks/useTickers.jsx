import { useEffect, useState } from "react";
import { fetchTickers, addTicker } from "../pages/Tickers/index.js"

const useTickers = (initialData) => {
  const [tickers, setTickers] = useState(initialData?.tickers || []);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (initialData) {
      setTickers(initialData.tickers);
    } else {
      setTickers([]);
    }
  }, [initialData]);

  const toggleTicker = async () => {
    //
  }


  const addNewTicker = async (ticker) => {
    try {
      const response = await addTicker(ticker);
      if (response?.tickers) {
        setError("")
        setTickers(response.tickers);
        return response;
      }
      throw new Error("Unexpected response structure");
    } catch (error) {
      setError("Failed to add ticker. Please try again.");
      throw error;
    }
  };

  return { tickers, setTickers, addNewTicker, error };
};

export default useTickers;
