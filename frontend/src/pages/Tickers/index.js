import axiosInstance from "../../utils/axios"

export const fetchTickers = () => {
    return axiosInstance.get("/tickers");
}

export const addTicker = (ticker) => {
    axiosInstance.post("/tickers", {
        ticker,
    }).then((it) => console.log(it))
}   

export const toggleTickerActive = (active, id) => {
    axiosInstance.put(`/toggle/${id}`, {
    }).then((it) => console.log(it))
}

export const deleteTicker = (id) => {
    axiosInstance.delete(`/tickers/${id}`)
}

export const asyncTickerValidation = (ticker) => {
    throw Error("Not yet implemented!")
    // axiosInstanc
}