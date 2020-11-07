import React, { FunctionComponent } from "react";
import style from "./SelectionBox.module.scss";

interface SelectionBoxProps {
    children?: string;
    onClick: () => void;
}

const SelectionBox: FunctionComponent<SelectionBoxProps> = (
    props: SelectionBoxProps
) => {
    return (
        <div className={style.box} onClick={props.onClick}>
            {props.children}
        </div>
    );
};

export default SelectionBox;
