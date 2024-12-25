import axiosInstance from "../../utils/axios"

export const fetchTickers = () => {
    axiosInstance.get("", {
        // 
    })
}

export const addTicker = (ticker) => {
    axiosInstance.post("/tickers", {
        ticker,
    })
}   

export const toggleTickerActive = (active, id) => {
    axiosInstance.put("/tickers", {
        active,
        id
    })
}

export const deleteTicker = (id) => {
    axiosInstance.delete(`/tickers/${id}`)
}
