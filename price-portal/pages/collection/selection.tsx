import React, { FunctionComponent, useState, useEffect } from "react";
import { useRouter } from "next/router";
import * as selections from "./selections.json";

import PageHeader from "../../components/PageHeader";
import SelectionBox from "../../components/base/SelectionBox";

export interface CollectionSelectionProps {}

const CollectionSelection: FunctionComponent<CollectionSelectionProps> = (
    props: CollectionSelectionProps
) => {
    const router = useRouter();
    const parsed = JSON.parse(JSON.stringify(selections));

    const table = () => {
        return (
            <div>
                {parsed.default.map((s, i) => {
                    return (
                        <SelectionBox
                            key={s.id}
                            onClick={() => {
                                router.push(`/collection/${s.id}`);
                            }}
                        >
                            {s.name}
                        </SelectionBox>
                    );
                })}
            </div>
        );
    };

    return (
        <>
            <PageHeader />
            <div style={{ paddingTop: "20px", fontSize: "30px" }}>
                Your Collections
            </div>
            {table()}
        </>
    );
};

export default CollectionSelection;
