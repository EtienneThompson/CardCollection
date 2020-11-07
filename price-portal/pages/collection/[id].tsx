import React, { FunctionComponent } from "react";
import * as collection from "./ShockLands.json";

import PageHeader from "../../components/PageHeader";
import CollectionHeader from "../../components/collection/CollectionHeader";
import DataTable from "../../components/base/dataTable/DataTable";

export interface CollectionHomeProps {}

const CollectionHome: FunctionComponent<CollectionHomeProps> = (
    props: CollectionHomeProps
) => {
    const parsed = JSON.parse(JSON.stringify(collection));

    const headers = [
        "Name",
        "Set",
        "Quantity",
        "Individual Price",
        "Total Price",
    ];

    const fetchPrices = () => {
        let total = 0;
        for (const item of parsed.default) {
            total += parseFloat(item.totalPrice);
        }
        return Math.round(total * 100) / 100;
    };

    return (
        <>
            <PageHeader />
            <CollectionHeader name={"ShockLands"} />

            <div
                style={{ paddingTop: 20, fontSize: "18px", fontWeight: "bold" }}
            >
                Total Price: ${fetchPrices()}
            </div>
            <DataTable headers={headers} items={parsed.default} />
        </>
    );
};

export default CollectionHome;
