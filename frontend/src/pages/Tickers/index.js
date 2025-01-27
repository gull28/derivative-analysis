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

export const toggleTickerActive = (id) => {
  axiosInstance.put(`/tickers/${id}/toggle`, {}).then((it) => console.log(it));
};

export const deleteTicker =  async (id) => {
  try {
    const response = await axiosInstance.delete(`/tickers/${id}`)

    console.log("resp", response)
    return response.data;
  }catch(error) {
    console.error("Error deleting ticker: ", error)
    throw error;
  }
};

export const asyncTickerValidation = (ticker) => {
  throw Error("Not yet implemented!");
};
