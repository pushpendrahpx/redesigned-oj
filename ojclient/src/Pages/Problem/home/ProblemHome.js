import React from "react"
function ProblemHome(props){
    console.log(props)
    return <div>
        {props?.problemDescription}
    </div>
}
export default ProblemHome