import { useEffect, useState } from "react";

const withData = (WrappedComponent, getDataFunc) => {
    return (props) => {
        const [response, setResponse] = useState();

        useEffect(() => {
            const fetchData = async () => {
                try {
                    const result = await getDataFunc();
                    setResponse(result);
                } catch (error) {
                    console.error("Error fetching data:", error);
                }
            };

            fetchData();
        }, []);

        if(!response){
            return <div>Loading</div>;
        }

        console.log(response.data)
        return <WrappedComponent {...props} data={response.data} />;
    };
};

export default withData;
