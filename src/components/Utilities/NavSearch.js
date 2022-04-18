import { Navbar, FormGroup, FormControl, Button } from "react-bootstrap";

export default function NavSearch() {
  return (
    <Navbar.Form pullLeft>
      <FormGroup>
        <FormControl type="text" placeholder="Search" />
      </FormGroup>{" "}
      <Button type="submit">Submit</Button>
    </Navbar.Form>
  );
}
