import React, { FunctionComponent } from "react";
import style from "./Container.module.scss";

export interface ContainerProps {
    children?: any[];
}

const Container: FunctionComponent<ContainerProps> = (
    props: ContainerProps
) => {
    const childrenJSX =
        props.children &&
        props.children.map((c, i) => {
            return <div key={i}>{c}</div>;
        });

    return <div className={style.container}>{childrenJSX}</div>;
};

export default Container;
