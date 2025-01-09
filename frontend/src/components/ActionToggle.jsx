import React, { useState } from "react";
import "./components.css";

const ActionToggle = ({ initialState = false, onChange }) => {
  const [checked, setChecked] = useState(initialState);

  const handleChange = () => {
    const newChecked = !checked;
    setChecked(newChecked);
    if (onChange) {
      onChange(newChecked);
    }
  };

  return (
    <div
      className={`toggle-container ${checked ? "checked" : ""}`}
      onClick={handleChange}
    >
      <div className="toggle-switch" />
    </div>
  );
};

export default ActionToggle;
