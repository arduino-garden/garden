package Cassandra

// This
type Pot struct {
	PotID string `json:"id,omitempty"`
}

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
