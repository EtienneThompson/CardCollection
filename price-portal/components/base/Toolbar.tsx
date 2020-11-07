import React, { FunctionComponent } from "react";
import style from "./Toolbar.module.scss";

interface ToolbarProps {
    children?: FunctionComponent[];
}

const Toolbar: FunctionComponent<ToolbarProps> = (props: ToolbarProps) => {
    const childrenJSX =
        props.children &&
        props.children.map((c, i) => {
            return <div key={i}>{c}</div>;
        });

    return (
        <div className={style.toolbar}>
            {childrenJSX}
            <div style={{ clear: "both" }}></div>
        </div>
    );
};

export default Toolbar;
