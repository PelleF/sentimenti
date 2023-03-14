import React, {useState} from 'react';
import {MakeCall} from "components/Body/MakeCall.js";

const Search = () => {

    const [searchInput, setSearchInput] = useState(null);
    const [searchResult, setSearchResult] = useState(null);

    // Set value in state
    const handleChange = (e) => {
      e.preventDefault();
      setSearchInput(e.target.value);
    };

    const handleSubmit = (e) => {
      MakeCall(searchInput).then(result => setSearchResult(result));
      e.preventDefault();
      console.log("Search result: " + searchResult)
      console.log(searchResult[0].value)
    };

     // To display result
     function formattedResult() {
        // Only show results if call is made
        if (searchResult === null) {
            console.log("searchResult was null")
            return ;
        } else {
            console.log("Mapping found result to html: " + searchResult)
            return <table>
                      <tr>
                        <th>Score</th>
                        <th>Title</th>
                      </tr>
                      <tr>
                        <td>{searchResult[0].score}</td>
                        <td><a href={searchResult[0].url} target="_blank">{searchResult[0].title}</a></td>
                      </tr>
                      <tr>
                        <td>{searchResult[1].score}</td>
                        <td><a href={searchResult[1].url} target="_blank">{searchResult[1].title}</a></td>
                      </tr>
                      <tr>
                        <td>{searchResult[2].score}</td>
                        <td><a href={searchResult[2].url} target="_blank">{searchResult[2].title}</a></td>
                      </tr>

                    </table>
        }
     }
                      // This is for the jokes
                      //<tr>
                      //  <td>{searchResult.id}</td>
                      //  <td><a href={searchResult.url} target="_blank">{searchResult.url}</a></td>
                      //  <td>{searchResult.value}</td>
                      //</tr>
     const resultTable = formattedResult();

    return (
            <div>
                <form>
                  <input type="text" onChange={handleChange} />
                  <input type="submit" value="Submit" onClick={handleSubmit} />
                </form>
                {resultTable}
            </div>
            );
};

            // <ul>
            //   {useState.results.Object.map(result => (
            //     <li key={result.id}>
            //       {result.url} {result.value}
            //     </li>
            //   ))}
            // </ul>


export default Search