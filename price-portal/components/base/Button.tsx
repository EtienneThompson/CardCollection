import React, { FunctionComponent } from "react";
import style from "./Button.module.scss";

type Alignments = "inline-end" | "inline-start" | "left" | "none" | "right";

interface ButtonProps {
    align?: string;
    children?: string;
    onClick?: () => void;
}

const Button: FunctionComponent<ButtonProps> = (props: ButtonProps) => {
    const alignment = (props.align ? props.align : "none") as Alignments;

    return (
        <>
            <div
                style={{
                    float: alignment,
                    paddingLeft: "3px",
                    paddingRight: "3px",
                }}
            >
                <div className={style.button} onClick={props.onClick}>
                    {props.children}
                </div>
            </div>
        </>
    );
};

export default Button;
