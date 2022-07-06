import React from "react"
function ProblemHome(props){
    console.log(props)
    return <div>
        <pre style={{whiteSpace: "pre-wrap"}}>
        {props?.problemDescription}
        </pre>
    </div>
}
export default ProblemHome