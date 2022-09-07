import { useState } from 'react'

function BootstrapInput(props) {
  const { id, placeholder, labelText, value, onChange, type } = props

  return(
    <div className="mb-3">
      <label htmlFor={id} className="form-label">{labelText}</label>
      <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder}/>
    </div>
  )
}

function PostForm(props) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [requested_amount, setRequestedAmount] = useState('')
  const handleSubmit= (e) => {
    e.preventDefault();
}
    return (
      <form onSubmit={e => {handleSubmit(e)}}>
        <BootstrapInput
          id="title"
          placeholder="Title of your post"
          labelText="Title"
          value={title}
          onChange={e => setTitle(e.target.value)}
          type="text"/>
        <BootstrapInput
          id="description"
          placeholder="Description of your post"
          labelText="Description"
          value={description}
          onChange={e => setDescription(e.target.value)}
          type="text"/>
        <BootstrapInput
          id="requested_amount"
          placeholder="Donation Amount"
          labelText="Donation Goal"
          value={requested_amount}
          onChange={e => setRequestedAmount(e.target.value)}
          type="integer"/>
        <input 
          className='submitButton'
          type='submit' 
          value='Post donation' 
        />
      </form>
    )
}
export default PostForm