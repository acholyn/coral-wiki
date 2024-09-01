import { Nav, Navbar, Row, Col } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import "./NavBar.css";

export let navcontents = [
	{ label: "Home", extension: "/coral-wiki/" },
	{ label: "Contributors", extension: "/coral-wiki/contributors" },
	{ label: "About Us", extension: "/coral-wiki/about" },
	{ label: "Contact Us", extension: "/coral-wiki/contact" },
	{ label: "Search", extension: "/coral-wiki/search" },
];
export default function NavBar() {
	return (
		<Row fluid="true" className="me-auto border-bottom border-secondary">
			<Navbar
				bg="light"
				variant="light"
				className="justify-content-center navBar"
			>
				{" "}
				<Col xs={2} />
				<Col className="">
					<Nav className="navBar">
						{navcontents.map((page, i) => (
							<LinkContainer to={page.extension} key={i}>
								<Nav.Link className="navlink">{page.label}</Nav.Link>
							</LinkContainer>
						))}
					</Nav>
				</Col>
				<Col xs={2} />
			</Navbar>
		</Row>
	);
}
