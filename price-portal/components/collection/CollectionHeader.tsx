import React, { FunctionComponent } from "react";
import style from "./CollectionHeader.module.scss";

import Button from "../base/Button";

export interface CollectionHeaderProps {
    name: string;
}

const CollectionHeader: FunctionComponent<CollectionHeaderProps> = (
    props: CollectionHeaderProps
) => {
    return (
        <div className={style.container}>
            <div className={style.name}>{props.name}</div>
            <Button
                align={"right"}
                onClick={() => {
                    console.log("add");
                }}
            >
                Add cards
            </Button>
            <Button
                align={"right"}
                onClick={() => {
                    console.log("remove");
                }}
            >
                Remove cards
            </Button>
            <div style={{ clear: "both" }}></div>
        </div>
    );
};

export default CollectionHeader;
