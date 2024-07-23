const UserData = ({users}) =>{
    return(
        <>
        {
            users.map((curUser)=>
            {
                const {Current_Branch, Category,Enrollment_no,
                    choice1, Choice2, Choice3,Choice4,Choice5,Choice6,Choice7,Choice8, Cname, allotment_result, allotment_status
                    }= curUser;
                    const style = allotment_status === "Allotted" ? {backgroundColor:"green"} : {backgroundColor:'red'} ;
                return (
                    <tr key={Category}  >
                        <td>{Category}</td>
                        <td>{Cname}</td>
                        <td>{Current_Branch}</td>
                        <td>{Enrollment_no}</td>
                        <td>{choice1}</td>
                        <td>{Choice2}</td>
                        <td>{Choice3}</td>
                        <td>{Choice4}</td>
                        <td>{Choice5}</td>
                        <td>{Choice6}</td>
                        <td>{Choice7}</td>
                        <td>{Choice8}</td>


                        <td>{allotment_result}</td>
                        <td style={style}>{allotment_status}</td>
                    </tr>
                )
            })
        }
   
        </>
    )

}
export default UserData;