import React, { useState } from "react";

const ActionToggle = (initialState = false, action) => {
    const [checked, setChecked] = useState(initialState);

    return (
        <input type="checkbox" checked={checked} onChange={(event) => setChecked(event.target.value)}/>
    )
}

export default ActionToggle;