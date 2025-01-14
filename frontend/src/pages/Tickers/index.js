import { HttpStatusCode } from "axios";
import axiosInstance from "../../utils/axios";

export const fetchTickers = () => {
  return axiosInstance.get("/tickers");
};

export const addTicker = async (ticker) => {
  try {
    const response = await axiosInstance.post("/tickers", {
      ticker,
    });
    return response.data;
  } catch (error) {
    console.error("Error adding ticker:", error);
    throw error;
  }
};

export const toggleTickerActive = (active, id) => {
  axiosInstance.put(`/toggle/${id}`, {}).then((it) => console.log(it));
};

export const deleteTicker = (id) => {
  axiosInstance.delete(`/tickers/${id}`);
};

export const asyncTickerValidation = (ticker) => {
  throw Error("Not yet implemented!");
};
