resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_B1s"
  admin_username      = "azureuser"
  network_interface_ids = [azurerm_network_interface.test.id,]
  admin_ssh_key {
    username   = "azureuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC4p3GI6WS8jJuooTN5tyawTAzaL+OfnEqgq32HgmIjUc945TGsX8C3s+wvPwr1WU250te2vhCuuBQFQ9i/gNSL1w2dqGIF++upomUfkljT/rPid1Qw+eVBFvgkapHPhaCVhornFmZhliVrtMboVmXnhc0msnAeYN9lLOBm0Ch4UYweQMN+mh88CSKwtXldHo9WQAMqc04fbmjdclzA++BTxpOlM+mhhCAYF5fqW3c5fbeWmYHxm+Ds/G0jkxUk1ycGX+tiXFrt0C5OHGRwU1fH7G4dn7e4mHiFan2iY41BnQD26eKt5mONN30Zn4kE3s49KIfBVJMIFB3SPj+iAFPLVeaPzvExQsLUM7laft6g67L+eoJnaa8E6SavBMX2EvusDR+Lft5F5gJPTUuOQ/OkzZB6AVhOzyK6XuQk1ybIaLzLVFEe4/kS920ADPKjaRHDGekictAKbvg8sW943YjY4LGMyfAZ3By4EjGTfVNvhfX7Dh90uVbqaafUEiUdFGTtjHXoIcnplXnPGHVDMfvYJN6HLx/cTdxn+dIyzMtgN5CyOzF15MzsNRoykjOBDy/tpAFIXq473d/BA99VEFK3rhfPbbvWf5CJM+189OP/g2RZqxcxENQ8pzkLK5z/gNdGrP+p3RwMA/01kIPhWMKdVLe7ruItdlxUnRFT5RynbQ== IMHOFMI@CMTCL060485" #file("./id_rsa.pub") #"file("~/.ssh/id_rsa.pub")"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }
}
