package main

import (
	"fmt"

	"github.com/hailocab/gocassa"
)

type Measurement struct {
	MeasurementId  string `json:"id,omitempty"`
	EventTimestamp int64
	AirTemperature int32
	AirHumidity    int32
	SoilMoisture   int32
	Light          int32
	PlantID        string
	PotID          string
}

func main() {
	keySpace, err := gocassa.ConnectToKeySpace("arduino_garden", []string{"127.0.0.1"}, "", "")
	if err != nil {
		panic(err)
	}
	salesTable := keySpace.Table("measurements", &Measurement{}, gocassa.Keys{
		PartitionKeys: []string{"MeasurementId"},
	})

	result := Measurement{}
	if err := salesTable.Where(gocassa.Eq("Id", "sale-1")).ReadOne(&result).Run(); err != nil {
		panic(err)
	}
	fmt.Println(result)
}
