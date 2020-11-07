import React, { FunctionComponent } from "react";
import style from "./DataTable.module.scss";

import Container from "../Container";

export interface DataTableProps {
    headers: string[];
    items: any[];
}

const DataTable: FunctionComponent<DataTableProps> = (
    props: DataTableProps
) => {
    const headers = () => {
        return (
            <>
                <div className={style.header + " " + style.row}>
                    {props.headers.map((h, i) => {
                        return (
                            <div className={style.column} key={i}>
                                {h}
                            </div>
                        );
                    })}
                </div>
                <div style={{ clear: "left" }}></div>
            </>
        );
    };

    const entries = () => {
        return (
            <div>
                {props.items.map((e, i) => {
                    return (
                        <div className={style.row} key={i}>
                            {Object.keys(e).map((k, j) => {
                                return (
                                    <div className={style.column} key={j}>
                                        {k.toLocaleLowerCase().includes("price")
                                            ? "$"
                                            : ""}
                                        {e[k]}
                                    </div>
                                );
                            })}
                        </div>
                    );
                })}
            </div>
        );
    };

    return (
        <Container>
            {headers()}
            {entries()}
        </Container>
    );
};

export default DataTable;
