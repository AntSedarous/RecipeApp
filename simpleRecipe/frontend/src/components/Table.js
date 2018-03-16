import React from "react";
import PropTypes from "prop-types";
import shortid from "shortid";
import OneRow from './oneRow';

const uuid = shortid.generate;

const Table = ({ data }) =>
  !data.length ? null : (
    <div className="column">
      <h2 className="subtitle">
        Showing <strong>{data.length} items</strong>
      </h2>

      {data.map(el =>{
        return (
        <OneRow
          title={el.name}
          author={el.owner}
          img = {el.pic}
          key={el.pk.toString()}
          about={el.about}
        />


      )
      })}
    </div>
  );

Table.propTypes = {
  data: PropTypes.array.isRequired
};

export default Table;
